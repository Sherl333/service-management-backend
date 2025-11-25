# app/routers/members.py
from fastapi import APIRouter, Depends, status
from sqlmodel import Session
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
