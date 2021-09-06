from typing import List, Optional
from pydantic import BaseModel


class JobBase(BaseModel):

    title: str
    skill: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class JobCreate(JobBase):

    pass


class JobUpdate(JobBase):

    title: str
    skill: str
    description: Optional[str] = None


class Job(JobBase):
    job_id: int

    class Config:
        orm_mode = True
        


class UserBase(BaseModel):
    candidate_name: Optional[str] = None
    email: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):

    password: str


class User(UserBase):
    candidate_name: Optional[str] = None
    user_id: int
    is_active: bool
  #  applied_job: Optional[JobBase]  # = []

    class Config:
        orm_mode = True


class ApplyBase(BaseModel):
    email: str
    job_id: int


class ApplyList(ApplyBase):
    apply_job_id: int
    user_de: Optional[UserBase]
    job_de: Optional[JobBase]

    class Config:
        orm_mode = True
