# app/routers/members.py
from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select
from app.models import Member
from typing import List, Optional
from app import schemas, crud
from app.database import get_session

router = APIRouter(prefix="/members", tags=["members"])

@router.post("", response_model=schemas.MemberRead, status_code=status.HTTP_201_CREATED)
def create_member(member_in: schemas.MemberCreate, session: Session = Depends(get_session)):
    m = crud.create_member(session, name=member_in.name, phone=member_in.phone)
    return m

@router.get("", response_model=List[schemas.MemberRead])
def list_members(status: Optional[str] = None, session: Session = Depends(get_session)):
    return crud.list_members(session, status)

@router.get("/search")
def search_members(q: str, session: Session = Depends(get_session)):
    query = select(Member).where(
        (Member.name.ilike(f"%{q}%")) | (Member.phone.ilike(f"%{q}%"))
    )
    results = session.exec(query).all()
    return results

@router.get("/filter")
def filter_members(status: str, session: Session = Depends(get_session)):
    query = select(Member).where(Member.status == status)
    results = session.exec(query).all()
    return results