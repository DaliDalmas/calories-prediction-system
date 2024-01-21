from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal1, engine

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()

@app.get("/training_session/{training_session_id}", response_model=schemas.ReadTrainingSessions, tags=['training sessions'])
def get_training_session(training_session_id: int, db: Session = Depends(get_db)):
    db_training_session = crud.get_training_session(db=db, training_session_id=training_session_id)
    if db_training_session is None:
        raise HTTPException(status_code=404, detail="Training session not found")
    return db_training_session

@app.get("/training_sessions/", response_model=list[schemas.ReadTrainingSessions], tags=["training sessions"])
def get_training_sessions(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_training_sessions(db=db, skip=skip, limit=limit)

@app.post("/training_session/", response_model=schemas.ReadTrainingSessions, tags=["training sessions"])
def post_training_session(training_session: schemas.CreateTrainingSessions, db: Session = Depends(get_db)):
    return crud.create_training_session(db=db, training_session=training_session)