from sqlalchemy import Column, Integer, DateTime, String, Float

from database import Base

class TrainingSessions(Base):
    __tablename__ = 'training_sessions'

    id = Column(Integer, primary_key=True, index=True)
    session_type = Column(String)
    actual_calories_burned = Column(Float)
    predicted_calories_burned = Column(Float)
    climb = Column(Float)
    duration = Column(Float)
    distance = Column(Float)
    session_time = Column(DateTime)
