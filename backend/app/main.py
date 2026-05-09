"""
This is the file uvicorn runs.
Creates the FastAPI app.
Loads settings.
Includes routers.
Sets up middleware (CORS, logging, etc.)
"""

from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI()

app.include_router(health_router, prefix="/api/v1")
