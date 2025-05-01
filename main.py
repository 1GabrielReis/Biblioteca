import sys
import os

from fastapi import FastAPI
from .api.rotas import router

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()
app.include_router(router)
