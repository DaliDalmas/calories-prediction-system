from sqlalchemy.orm import Session

import models, schemas

def get_training_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TrainingSessions).offset(skip).limit(limit).all()

def get_training_session(db: Session, training_session_id: int):
    return db.query(models.TrainingSessions).filter(models.TrainingSessions.id==training_session_id).first()

def create_training_session(db: Session, training_session: schemas.CreateTrainingSessions):
    db_training_session = models.TrainingSessions(
        session_type = training_session.session_type,
        actual_calories_burned = training_session.actual_calories_burned,
        predicted_calories_burned = training_session.predicted_calories_burned,
        climb = training_session.climb,
        duration = training_session.duration,
        distance = training_session.distance,
        session_time = training_session.session_time
    )

    db.add(db_training_session)
    db.commit()
    db.refresh(db_training_session)
    return db_training_session

