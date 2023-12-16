from pydantic import BaseModel
from typing import Optional

class Events(BaseModel):
    EventID: int
    name: str
    date: str
    Time: str
    Location: str
    TicketPrice: float

class EventInput(BaseModel):
    EventID: int
    name: Optional[str] = None
    date: str

class NewId(BaseModel):
    code: int
    EventID: int

class EventDelete(BaseModel):
    code: int
    EventID: int
