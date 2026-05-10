from pydantic import BaseModel

class StudentInput(BaseModel):
    hours_studied: float