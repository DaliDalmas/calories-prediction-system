from pydantic import BaseModel
from datetime import datetime

class ReadTrainingSessions(BaseModel):
    id: int
    session_type: str
    actual_calories_burned: float
    predicted_calories_burned: float
    climb: float
    duration: float
    distance: float
    session_time: datetime

    class Config:
        orm_mode = True

class CreateTrainingSessions(BaseModel):
    session_type: str
    actual_calories_burned: float
    climb: float
    duration: float
    distance: float
    session_time: datetime

