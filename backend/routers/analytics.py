from fastapi import APIRouter
from core.supabase_client import supabase

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/college/{company_id}")
async def college_analytics(company_id: str):
    res = supabase.rpc("college_analytics_for_company", {"cid": company_id}).execute()
    # fallback direct query
    res = (
        supabase.table("session_reports")
        .select("college,hire_signal,overall_score,lc_score,rw_score,conceptual_score")
        .eq("company_id", company_id)
        .execute()
    )
    rows = res.data
    from collections import defaultdict
    agg = defaultdict(lambda: {"total":0,"hired":0,"scores":[]})
    for r in rows:
        col = r.get("college") or "Unknown"
        agg[col]["total"] += 1
        if r["hire_signal"] in ["strong_yes","yes","lean_yes"]:
            agg[col]["hired"] += 1
        agg[col]["scores"].append(r.get("overall_score") or 0)
    result = []
    for col, d in agg.items():
        result.append({
            "college":      col,
            "total":        d["total"],
            "hired":        d["hired"],
            "hire_rate":    round(d["hired"]/d["total"]*100,1) if d["total"] else 0,
            "avg_score":    round(sum(d["scores"])/len(d["scores"]),2) if d["scores"] else 0,
        })
    return sorted(result, key=lambda x: x["hire_rate"], reverse=True)

@router.get("/company/{company_id}/summary")
async def company_summary(company_id: str):
    res = supabase.table("session_reports").select("hire_signal,overall_score,lc_score,rw_score").eq("company_id", company_id).execute()
    rows = res.data
    if not rows:
        return {"total": 0}
    hired = sum(1 for r in rows if r["hire_signal"] in ["strong_yes","yes","lean_yes"])
    return {
        "total_interviews": len(rows),
        "total_hired":      hired,
        "hire_rate_pct":    round(hired/len(rows)*100,1),
        "avg_overall":      round(sum(r["overall_score"] or 0 for r in rows)/len(rows),2),
        "avg_lc":           round(sum(r["lc_score"] or 0 for r in rows)/len(rows),2),
        "avg_rw":           round(sum(r["rw_score"] or 0 for r in rows)/len(rows),2),
    }