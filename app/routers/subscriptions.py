# app/routers/subscriptions.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app import schemas, crud
from app.database import get_session
from typing import Optional

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

@router.post("", response_model=schemas.SubscriptionRead)
def create_subscription(sub_in: schemas.SubscriptionCreate, session: Session = Depends(get_session)):
    return crud.create_subscription(session, sub_in.member_id, sub_in.plan_id, sub_in.start_date)

@router.get("/members/{member_id}/current-subscription", response_model=Optional[schemas.SubscriptionRead])
def get_current_subscription(member_id: int, session: Session = Depends(get_session)):
    sub = crud.get_current_subscription(session, member_id)
    if not sub:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="No active subscription for this member")
    return sub
