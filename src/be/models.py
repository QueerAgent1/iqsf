from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SafetyReport(BaseModel):
    id: Optional[int] = None
    zip: str
    identity: str
    report: str
    consent: str
    created_at: Optional[datetime] = None

class Score(BaseModel):
    id: Optional[int]
    zip: str
    identity: str
    value: float
    rationale: Optional[str]
    generated_at: Optional[datetime] = None

class Persona(BaseModel):
    id: Optional[int]
    type: str
    description: Optional[str]