from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
import datetime

class Member(SQLModel, table=True):
    __tablename__ = "member"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    phone: str = Field(sa_column_kwargs={"unique": True})
    join_date: datetime.date = Field(default_factory=lambda: datetime.date.today())
    status: str = Field(default="active")  # active / inactive
    total_check_ins: int = Field(default=0)

    subscriptions: List["Subscription"] = Relationship(back_populates="member")
    attendance_records: List["Attendance"] = Relationship(back_populates="member")


class Plan(SQLModel, table=True):
    __tablename__ = "plan"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    duration_days: int

    subscriptions: List["Subscription"] = Relationship(back_populates="plan")


class Subscription(SQLModel, table=True):
    __tablename__ = "subscription"
    id: Optional[int] = Field(default=None, primary_key=True)
    member_id: int = Field(foreign_key="member.id")
    plan_id: int = Field(foreign_key="plan.id")
    start_date: datetime.date
    end_date: datetime.date

    member: Optional[Member] = Relationship(back_populates="subscriptions")
    plan: Optional[Plan] = Relationship(back_populates="subscriptions")


class Attendance(SQLModel, table=True):
    __tablename__ = "attendance"
    id: Optional[int] = Field(default=None, primary_key=True)
    member_id: int = Field(foreign_key="member.id")
    check_in_time: Optional[datetime.datetime] = Field(default_factory=lambda: datetime.datetime.utcnow())

    member: Optional[Member] = Relationship(back_populates="attendance_records")
