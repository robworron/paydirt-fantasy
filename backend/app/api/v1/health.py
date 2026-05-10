"""
Contains the /health endpoint.
Used for monitoring, uptime checks, and debugging.
Provides a simple endpoint to check to see if the API is alive.
Used by load balancers, uptime monitors, AWS health checks.

(EXAMPLE ENDPOINT:
GET /api/v1/health)
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}

