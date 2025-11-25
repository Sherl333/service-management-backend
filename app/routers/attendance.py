# app/routers/attendance.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app import schemas, crud
from app.database import get_session
from typing import List

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/check-in", response_model=schemas.AttendanceRead)
def check_in(at_in: schemas.AttendanceCreate, session: Session = Depends(get_session)):
    return crud.record_attendance(session, at_in.member_id)

@router.get("/members/{member_id}/attendance", response_model=List[schemas.AttendanceRead])
def list_attendance(member_id: int, session: Session = Depends(get_session)):
    return crud.list_attendance(session, member_id)
