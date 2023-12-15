from pydantic import BaseModel
from typing import Optional

class ConcertVenue(BaseModel):
    concert_id: int
    name: str
    location: Optional[str] = None

class ConcertVenueInput(BaseModel):
    name: str
    location: Optional[str] = None

class NewId(BaseModel):
    code: int
    id: int

class DeleteItem(BaseModel):
    code: int
    id: int