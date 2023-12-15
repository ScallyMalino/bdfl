from Server.Events.models import Events, EventInput, NewId, EventDelete
from typing import List
from Server.db_manager import base_manager

def get_events() -> List[Events]:
    res = base_manager.execute("SELECT EventID, name, date, Time, Location, TicketPrice FROM Events", many=True)
    data = res.get('data',[])
    return [Events(EventID=item[0], name=item[1], date=item[2], Time=item[3], Location=item[4], TicketPrice=item[5]) for item in data]

def add_eventse(Events: EventInput) -> NewId:
    res = base_manager.execute("INSERT INTO Events(name, date, Time, Location, TicketPrice) VALUES (?, ?) RETURNING EventID",
                               args=(Events.name, Events.date,Events.Time,Events.Location, Events.TicketPrice))
    return NewId(code=res['code'], id=res['data'][0][0][0][0][0])

def delete_events(EventID: int) -> EventDelete:
    res = base_manager.execute("DELETE FROM Events WHERE EventID = ?", args=(EventID))
    return EventDelete(code=res['code'], id=EventID)