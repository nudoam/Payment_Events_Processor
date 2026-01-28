# app/services/processor.py
from app.models.schemas import PaymentEventCreate
from app.services.repository import PaymentEventRepository

class PaymentProcessor:
    def __init__(self, repo: PaymentEventRepository):
        self.repo = repo

    def create_event(self, dto: PaymentEventCreate):
        return self.repo.create(dto)

    def get_event(self, event_id: str):
        return self.repo.get(event_id)
