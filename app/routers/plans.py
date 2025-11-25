# app/routers/plans.py
from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List
from app import schemas, crud
from app.database import get_session

router = APIRouter(prefix="/plans", tags=["plans"])

@router.post("", response_model=schemas.PlanRead, status_code=status.HTTP_201_CREATED)
def create_plan(plan_in: schemas.PlanCreate, session: Session = Depends(get_session)):
    return crud.create_plan(session, plan_in.name, plan_in.price, plan_in.duration_days)

@router.get("", response_model=List[schemas.PlanRead])
def list_plans(session: Session = Depends(get_session)):
    return crud.list_plans(session)
