from typing import List
from fastapi import APIRouter
from Server.concert_venues.models import (ConcertVenue, ConcertVenueInput, NewId, DeleteItem)
from Server.concert_venues.resolvers import get_concert_venues as resolver_get_concert_venues, add_concert_venue, delete_concert_venue

router = APIRouter()

@router.get('/get/', response_model=List[ConcertVenue])
def get_concert_venues():
    return resolver_get_concert_venues()

@router.post('/post/', response_model=NewId)
def add_user_endpoint(concert_venue: ConcertVenueInput):
    return add_concert_venue(concert_venue)

@router.delete("/delete/{concert_id}")
def delete_concert(concert_id: str) -> DeleteItem:
    return delete_concert_venue(concert_id)