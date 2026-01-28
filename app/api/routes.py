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
    return created

@router.get("/events/{event_id}", response_model=PaymentEvent)
def get_event(event_id: str, processor: PaymentProcessor = Depends(get_processor)):
    found = processor.get_event(event_id)
    if not found:
        raise HTTPException(status_code=404, detail="Event not found")
    return found
