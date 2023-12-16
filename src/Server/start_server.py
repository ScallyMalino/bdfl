import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Users.routers import router as users_router
from concert_venues.routers import router as concert_venues_router
from Events.routers import router as events_router
from db_manager import base_manager
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH

app = FastAPI()

app.include_router(users_router, prefix='/users')
app.include_router(concert_venues_router, prefix='/concert_venues')
app.include_router(events_router, prefix='/events')

@app.get('/')
def root():
    return RedirectResponse('/docs')

if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1", port=8000, reload=True)