# app/services/repository.py
from sqlalchemy.orm import Session
from app.models.db_models import PaymentEventDB
from app.models.schemas import PaymentEventCreate

class PaymentEventRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, dto: PaymentEventCreate) -> PaymentEventDB:
        obj = PaymentEventDB(
            event_type=dto.event_type,
            payment_id=dto.payment_id,
            amount=dto.amount,
            currency=dto.currency,
            metadata=dto.metadata,
        )
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, event_id: str) -> PaymentEventDB | None:
        return self.db.get(PaymentEventDB, event_id)
