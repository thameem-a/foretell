from fastapi import FastAPI

from app.api.v1.kalshi import router as kalshi_router


app = FastAPI()

app.include_router(kalshi_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return "Welcome to Fortell!"

@app.get("/health")
def health_check():
    return {"Health" : "ok"}
