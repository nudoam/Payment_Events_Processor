# app/models/schemas.py
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class PaymentEventCreate(BaseModel):
    event_type: str = Field(min_length=3, max_length=64)
    payment_id: str = Field(min_length=3, max_length=64)
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=8)
    meta: dict | None = Field(default=None, validation_alias="metadata")


    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, v: str) -> str:
        return v.upper()

class PaymentEvent(BaseModel):
    id: str
    event_type: str
    payment_id: str
    amount: float
    currency: str
    meta: dict | None = Field(default=None, serialization_alias="metadata")
    created_at: datetime

    class Config:
        from_attributes = True
