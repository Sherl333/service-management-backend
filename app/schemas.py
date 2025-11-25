# app/schemas.py
from pydantic import BaseModel, Field, constr
import datetime
from typing import Optional, List

# Member
class MemberCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    phone: constr(strip_whitespace=True, min_length=7)

class MemberRead(BaseModel):
    id: int
    name: str
    phone: str
    join_date: datetime.date
    status: str
    total_check_ins: int

    class Config:
        orm_mode = True

# Plan
class PlanCreate(BaseModel):
    name: str
    price: float = Field(..., ge=0)
    duration_days: int = Field(..., gt=0)

class PlanRead(BaseModel):
    id: int
    name: str
    price: float
    duration_days: int

    class Config:
        orm_mode = True

# Subscription
class SubscriptionCreate(BaseModel):
    member_id: int
    plan_id: int
    start_date: datetime.date

class SubscriptionRead(BaseModel):
    id: int
    member_id: int
    plan_id: int
    start_date: datetime.date
    end_date: datetime.date

    class Config:
        orm_mode = True

# Attendance
class AttendanceCreate(BaseModel):
    member_id: int

class AttendanceRead(BaseModel):
    id: int
    member_id: int
    check_in_time: datetime.datetime

    class Config:
        orm_mode = True
