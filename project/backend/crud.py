from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):

    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password,candidate_name=user.candidate_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_delete(db: Session, user_id: int):

    return db.query(models.User).filter(models.User.user_id == user_id).all()

def user_update(db: Session, user_id: int):

    return db.query(models.User).filter(models.User.user_id == user_id).all()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Job).offset(skip).limit(limit).all()

def create_user_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def apply_for_jobs(db: Session, apply : schemas.ApplyBase):
    db_apply = models.Apply(**apply.dict())
    db.add(db_apply)
    db.commit()
    db.refresh(db_apply)
    return db_apply

def job_update(db: Session,job:schemas.JobUpdate,job_id: int):

    db_job =db.query(models.Job).filter(models.Job.job_id==job_id).first()
    for var, value in vars(job).items():
        setattr(db_job, var, value) if value else None
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def job_delete(db: Session, job_id: int):

    db_job = db.query(models.Job).filter(models.Job.job_id== job_id).first()
    db.delete(db_job)
    db.commit()
    return "success"


def get_list(db: Session, job_id: int):

    return db.query(models.Apply).filter(models.Apply.job_id == job_id).all()