from fastapi import APIRouter, HTTPException
from core.supabase_client import supabase
from models.schemas import CompanyCreate, RequirementsCreate

router = APIRouter(prefix="/companies", tags=["companies"])

@router.post("/")
async def create_company(data: CompanyCreate):
    res = supabase.table("companies").insert(data.model_dump()).execute()
    return res.data[0]

@router.get("/{company_id}")
async def get_company(company_id: str):
    res = supabase.table("companies").select("*").eq("id", company_id).execute()
    if not res.data:
        raise HTTPException(404, "Not found")
    return res.data[0]

@router.post("/requirements")
async def create_requirements(data: RequirementsCreate):
    res = supabase.table("company_requirements").insert(data.model_dump()).execute()
    return res.data[0]

@router.get("/{company_id}/requirements")
async def get_requirements(company_id: str):
    res = (
        supabase.table("company_requirements")
        .select("*")
        .eq("company_id", company_id)
        .eq("is_active", True)
        .execute()
    )
    return res.data
