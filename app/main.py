from fastapi import FastAPI

app = FastAPI(title="Payment Events Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}
