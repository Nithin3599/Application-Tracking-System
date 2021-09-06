from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    candidate_name = Column(String)
    is_active = Column(Boolean, default=True)

    applied_jobs = relationship("Apply")
   


class Job(Base):

    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    skill = Column(String, index=True)
    description = Column(String, index=True)
   

class Apply(Base):

    __tablename__ = "apply"

    apply_job_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, ForeignKey("users.email"))
    job_id = Column(Integer, ForeignKey("jobs.job_id"))

    user_de = relationship('User', foreign_keys=[email])
 #   user_de = relationship("Job",back_populates=" applied_jobs")
    job_de = relationship("Job")
