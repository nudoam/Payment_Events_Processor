# app/main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Payment Events Processor")
app.include_router(router)
