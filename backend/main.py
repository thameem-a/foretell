from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to Fortell!"

@app.get("/health")
def health_check():
    return {"Health" : "ok"}
