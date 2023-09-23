from fastapi import FastAPI

app = FastAPI()

events = [
    {"id": 1, "name": "Концерт 1", "location": "Место 1"},
    {"id": 2, "name": "Концерт 2", "location": "Место 2"},
]


@app.get('/events')
def get_events():
    return events

@app.get('/events/{event_id}')
def get_event(event_id: int):
    event = next((e for e in events if e["id"] == event_id), None)
    if event is None:
        return {"message": "Мероприятие не найдено"}
    return event

@app.post('/events')
def create_event(event: dict):
    event_id = max(e["id"] for e in events) + 1
    event["id"] = event_id
    events.append(event)
    return {"message": "Мероприятие создано", "event_id": event_id}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
