from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, query


from . import crud, models, schemas
from .database import SessionLocal, engine



models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = [
    "http://localhost:8081",
     "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User,tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User],tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User,tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/jobs/", response_model=schemas.Job,tags=["Jobs"])
def create_job(
    job: schemas.JobCreate, db: Session = Depends(get_db)
):
    return crud.create_user_job(db=db, job=job)


@app.get("/jobs/", response_model=List[schemas.Job],tags=["Jobs"])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs

@app.put("/jobs/{job_id}",response_model=schemas.JobUpdate,tags=["Jobs"])
def update_job(job:schemas.JobUpdate,job_id=int,  db: Session = Depends(get_db)):

    return crud.job_update(db=db,job_id=job_id,job=job)

@app.delete("/jobs/{job_id}/", tags=["Jobs"])
def delete_job(job_id:int,db: Session = Depends(get_db)):
   db_delete = crud.job_delete(db, job_id=job_id)

   return db_delete

@app.post("/apply/users/",tags=["Apply"])
def apply_for_jobs(apply_job: schemas.ApplyBase,db: Session = Depends(get_db)):

    return crud.apply_for_jobs(db,apply_job)

@app.get("/apply/{job_id}/users",response_model=List[schemas.ApplyList],tags=["Apply"])
def apply_list(job_id: int, db: Session = Depends(get_db)):
    db_list = crud.get_list(db, job_id=job_id)

    if db_list is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_list