from sqlmodel import Session, select
from app import models
import datetime
from fastapi import HTTPException
from typing import Optional, List

def create_member(session: Session, name: str, phone: str) -> models.Member:
    existing = session.exec(select(models.Member).where(models.Member.phone == phone)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone already registered")
    member = models.Member(name=name, phone=phone)
    session.add(member)
    session.commit()
    session.refresh(member)
    return member

def list_members(session: Session, status: Optional[str] = None) -> List[models.Member]:
    stmt = select(models.Member)
    if status:
        stmt = stmt.where(models.Member.status == status)
    return session.exec(stmt).all()

def create_plan(session: Session, name: str, price: float, duration_days: int) -> models.Plan:
    plan = models.Plan(name=name, price=price, duration_days=duration_days)
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan

def list_plans(session: Session):
    return session.exec(select(models.Plan)).all()

def get_plan(session: Session, plan_id: int) -> models.Plan:
    plan = session.get(models.Plan, plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

def get_member(session: Session, member_id: int) -> models.Member:
    member = session.get(models.Member, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

def create_subscription(session: Session, member_id: int, plan_id: int, start_date: datetime.date):
    member = get_member(session, member_id)
    plan = get_plan(session, plan_id)
    end_date = start_date + datetime.timedelta(days=plan.duration_days)
    sub = models.Subscription(member_id=member_id, plan_id=plan_id, start_date=start_date, end_date=end_date)
    session.add(sub)
    session.commit()
    session.refresh(sub)
    return sub

def get_current_subscription(session: Session, member_id: int) -> Optional[models.Subscription]:
    today = datetime.date.today()
    stmt = select(models.Subscription).where(
        (models.Subscription.member_id == member_id)
        & (models.Subscription.start_date <= today)
        & (models.Subscription.end_date >= today)
    )
    return session.exec(stmt).first()

def record_attendance(session: Session, member_id: int):
    # verify member exists
    member = get_member(session, member_id)
    sub = get_current_subscription(session, member_id)
    if not sub:
        raise HTTPException(status_code=400, detail="No active subscription for this member")
    attendance = models.Attendance(member_id=member_id)
    session.add(attendance)
    session.commit()
    session.refresh(attendance)
    # Note: total_check_ins will be incremented by DB trigger (preferred)
    return attendance

def list_attendance(session: Session, member_id: int):
    stmt = select(models.Attendance).where(models.Attendance.member_id == member_id).order_by(models.Attendance.check_in_time.desc())
    return session.exec(stmt).all()
