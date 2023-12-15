from typing import List
from fastapi import APIRouter
from Server.Events.models import (Events, EventInput, NewId, EventDelete)
from Server.Events.resolvers import get_events as resolver_get_concert_venues, add_eventse, delete_events

router = APIRouter()

@router.get('/get/', response_model=List[Events])
def get_concert_venues():
    return resolver_get_concert_venues()

@router.post('/post/', response_model=NewId)
def add_user_endpoint(Events: EventInput):
    return add_eventse(Events)

@router.delete("/delete/{EventID}")
def delete_concert(EventID: int) -> EventDelete:
    return delete_events(EventID)