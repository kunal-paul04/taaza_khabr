from fastapi import FastAPI
from app.routes.routes import route
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(route)
