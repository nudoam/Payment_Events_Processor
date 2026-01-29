# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Payment Events Processor"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5433/payment_events"

settings = Settings()
