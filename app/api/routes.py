# app/api/routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.schemas import PaymentEventCreate, PaymentEvent
from app.services.repository import PaymentEventRepository
from app.services.processor import PaymentProcessor

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

def get_processor(db: Session = Depends(get_db)) -> PaymentProcessor:
    repo = PaymentEventRepository(db)
    return PaymentProcessor(repo)

@router.post("/events", response_model=PaymentEvent, status_code=status.HTTP_201_CREATED)
def create_event(payload: PaymentEventCreate, processor: PaymentProcessor = Depends(get_processor)):
    created = processor.create_event(payload)

    return PaymentEvent(
        id=created.id,
        event_type=created.event_type,
        payment_id=created.payment_id,
        amount=created.amount,
        currency=created.currency,
        meta=created.meta,
        created_at=created.created_at,
    )

@router.get("/events/{event_id}", response_model=PaymentEvent)
def get_event(event_id: str, processor: PaymentProcessor = Depends(get_processor)):
    found = processor.get_event(event_id)
    if not found:
        raise HTTPException(status_code=404, detail="Event not found")
    return found
