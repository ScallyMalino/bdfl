from Server.concert_venues.models import ConcertVenue, ConcertVenueInput, NewId, DeleteItem
from typing import List
from Server.db_manager import base_manager

def get_concert_venues() -> List[ConcertVenue]:
    res = base_manager.execute("SELECT concert_id, name, location FROM concert_venues", many=True)
    data = res.get('data',[])
    return [ConcertVenue(concert_id=item[0], name=item[1], location=item[2]) for item in data]

def add_concert_venue(concert_venue: ConcertVenueInput) -> NewId:
    res = base_manager.execute("INSERT INTO concert_venues(name, location) VALUES (?, ?) RETURNING concert_id",
                               args=(concert_venue.name, concert_venue.location))
    return NewId(code=res['code'], id=res['data'][0][0])

def delete_concert_venue(concert_id: str) -> DeleteItem:
    res = base_manager.execute("DELETE FROM concert_venues WHERE concert_id = ?", args=(concert_id,))
    return DeleteItem(code=res['code'], id=concert_id)
