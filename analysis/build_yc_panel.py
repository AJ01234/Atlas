"""Build a reproducible public-data YC panel and run proxy tests for H1-H5.

Important: this is NOT the final acceptance-time causal panel from Chapter 37.
YC's public directory does not expose all acceptance-time variables or funding
history. The script therefore separates observable proxy tests from claims that
require proprietary/hand-coded acceptance-time data.
"""
from __future__ import annotations
import json, math, re
from pathlib import Path
import pandas as pd
import numpy as np
import requests
import statsmodels.api as sm
from statsmodels.formula.api import logit, ols

ROOT = Path("analysis_output")
ROOT.mkdir(exist_ok=True)
URL = "https://yc-oss.github.io/api/companies/all.json"


def load():
    r = requests.get(URL, timeout=120)
    r.raise_for_status()
    data = r.json()
    df = pd.DataFrame(data)
    df.to_csv(ROOT / "yc_company_panel.csv", index=False)
    return df


def contains(text, words):
    t = str(text).lower()
    return int(any(w in t for w in words))


def prepare(df):
    df = df.copy()
    df["batch_year"] = df["batch"].astype(str).str.extract(r"(\d{2})$")[0].astype(float)
    df["batch_year"] = np.where(df["batch_year"] < 50, 2000 + df["batch_year"], 1900 + df["batch_year"])
    df["founder_count_proxy"] = np.nan  # not exposed by YC OSS directory
    df["ai_tag"] = df["tags"].apply(lambda x: int(any("artificial intelligence" == str(t).lower() or "generative ai" in str(t).lower() or "ai" == str(t).lower() for t in (x or []))))
    df["automation_tag"] = df["tags"].apply(lambda x: int(any("automation" in str(t).lower() or "robot" in str(t).lower() for t in (x or []))))
    df["workflow_text"] = (df["one_liner"].fillna("") + " " + df["long_description"].fillna(""))
    pain = ["reduce cost", "save time", "manual", "expensive", "labor", "workflow", "compliance", "back office", "automate", "automation", "bottleneck", "inefficient", "paperwork", "repetitive"]
    df["problem_leverage_proxy"] = df["workflow_text"].apply(lambda x: min(5, sum(str(x).lower().count(w) for w in pain)))
    df["problem_leverage_proxy"] = df["problem_leverage_proxy"].clip(0,5)
    df["technical_leverage_proxy"] = (df["ai_tag"] + df["automation_tag"]).clip(0, 2)
    df["outcome_success_proxy"] = ((df["status"].isin(["Public", "Acquired"])) | (df["top_company"].fillna(False)) | (pd.to_numeric(df["team_size"], errors="coerce").fillna(0) >= 100)).astype(int)
    df["survival_proxy"] = (~df["status"].isin(["Inactive", "Dead", "Shutdown"])).astype(int)
    return df


def run_tests(df):
    rows=[]
    # H1: founder capability. Public YC directory does not expose founder backgrounds/counts.
    rows.append({"hypothesis":"H1 Founder capability","status":"NOT TESTABLE from YC OSS alone","n":0,"model":"Requires founder-level panel (build/domain/execution/learning/complementarity).","result":"Deferred"})

    # H2: problem leverage proxy -> success proxy, controlling batch and industry.
    d=df.dropna(subset=["problem_leverage_proxy","outcome_success_proxy"]).copy()
    try:
        m=logit("outcome_success_proxy ~ problem_leverage_proxy + C(batch_year) + C(industry)", data=d).fit(disp=False)
        rows.append({"hypothesis":"H2 Problem leverage","status":"PROXY TEST","n":len(d),"model":"Logit(success proxy ~ problem leverage proxy + batch + industry)","coefficient":m.params.get("problem_leverage_proxy",np.nan),"p_value":m.pvalues.get("problem_leverage_proxy",np.nan),"result":"Supported" if m.pvalues.get("problem_leverage_proxy",1)<0.05 else "Not supported"})
    except Exception as e:
        rows.append({"hypothesis":"H2 Problem leverage","status":"PROXY TEST FAILED","n":len(d),"result":str(e)})

    # H3: AI leverage -> success proxy, with batch/industry controls.
    d=df.dropna(subset=["ai_tag","outcome_success_proxy"]).copy()
    try:
        m=logit("outcome_success_proxy ~ ai_tag + C(batch_year) + C(industry)", data=d).fit(disp=False)
        rows.append({"hypothesis":"H3 AI leverage","status":"PROXY TEST","n":len(d),"model":"Logit(success proxy ~ AI tag + batch + industry)","coefficient":m.params.get("ai_tag",np.nan),"p_value":m.pvalues.get("ai_tag",np.nan),"odds_ratio":math.exp(m.params.get("ai_tag",0)),"result":"Supported" if m.pvalues.get("ai_tag",1)<0.05 else "Not supported"})
    except Exception as e:
        rows.append({"hypothesis":"H3 AI leverage","status":"PROXY TEST FAILED","n":len(d),"result":str(e)})

    # H4: early-stage judgment. Public directory has no acceptance-time traction, so cannot test without leakage.
    rows.append({"hypothesis":"H4 Early-stage judgment","status":"NOT TESTABLE without acceptance-time traction","n":0,"model":"Requires revenue/users/growth/paying customers observed at or before YC acceptance.","result":"Deferred to acceptance-time panel"})

    # H5: venture-scale potential. Use top-company / public / acquired / team>=100 as a deliberately coarse outcome proxy.
    # Market scale proxy = technical/industry tags + description length, not TAM; this is only a stress test.
    d=df.dropna(subset=["outcome_success_proxy"]).copy()
    d["scale_proxy"]=(d["long_description"].fillna("").str.len()/1000).clip(0,5) + d["technical_leverage_proxy"]
    try:
        m=logit("outcome_success_proxy ~ scale_proxy + C(batch_year) + C(industry)", data=d).fit(disp=False)
        rows.append({"hypothesis":"H5 Venture-scale potential","status":"COARSE PROXY TEST","n":len(d),"model":"Logit(success proxy ~ scale proxy + batch + industry)","coefficient":m.params.get("scale_proxy",np.nan),"p_value":m.pvalues.get("scale_proxy",np.nan),"result":"Supported" if m.pvalues.get("scale_proxy",1)<0.05 else "Not supported"})
    except Exception as e:
        rows.append({"hypothesis":"H5 Venture-scale potential","status":"PROXY TEST FAILED","n":len(d),"result":str(e)})

    out=pd.DataFrame(rows)
    out.to_csv(ROOT / "hypothesis_results.csv", index=False)
    return out


def main():
    df=prepare(load())
    results=run_tests(df)
    meta={"rows":len(df),"source":URL,"research_cutoff":"2026-08-22","note":"Public-directory proxy panel; not the final acceptance-time causal dataset."}
    (ROOT/"panel_metadata.json").write_text(json.dumps(meta,indent=2))
    print(results.to_string(index=False))
    print(json.dumps(meta))

if __name__ == "__main__": main()
