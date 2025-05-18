from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.company.schema import CompanyRead, CompanyCreate, CompanyRead
from app.company.repository import get_company, get_companies, create_company
from app.core.database import get_db

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=CompanyRead, status_code=status.HTTP_201_CREATED)
async def add_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db=db, company=company)


@router.get("/", response_model=List[CompanyRead])
async def get_all_companies(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    companies = get_companies(db, skip=skip, limit=limit)
    return companies


@router.get("/{id}", response_model=CompanyRead)
async def get_company_endpoint(id: int, db: Session = Depends(get_db)):
    db_company = get_company(db, id)
    if db_company is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Company not found"
        )
    return db_company
