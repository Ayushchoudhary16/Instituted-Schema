from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class InstituteBase(BaseModel):
    name: str
    address: Optional[str] = None

class InstituteCreate(InstituteBase):
    pass

class InstituteResponse(InstituteBase):
    id: int
    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None
    institute_id: int

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    class Config:
        orm_mode = True


class BatchBase(BaseModel):
    name: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    course_id: int

class BatchCreate(BatchBase):
    pass

class BatchResponse(BatchBase):
    id: int
    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    batch_id: int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        orm_mode = True


class FeeBase(BaseModel):
    student_id: int
    total_fee: float
    paid_amount: Optional[float] = 0.0
    due_amount: Optional[float] = 0.0

class FeeCreate(FeeBase):
    pass

class FeeResponse(FeeBase):
    id: int
    class Config:
        orm_mode = True


class InstallmentBase(BaseModel):
    fee_id: int
    amount: float
    paid_on: Optional[date] = None

class InstallmentCreate(InstallmentBase):
    pass

class InstallmentResponse(InstallmentBase):
    id: int
    class Config:
        orm_mode = True
