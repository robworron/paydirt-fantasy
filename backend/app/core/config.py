"""
Loads environment variables such as database URL, S3 bucket name, secrets.
Central place for settings.
Uses Pydantic's BaseSettings
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
