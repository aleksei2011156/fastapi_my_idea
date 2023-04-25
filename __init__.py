from fastapi import FastAPI
from .core import crud, models, schemas, settings

app = FastAPI()

from .core.routers import registration_users