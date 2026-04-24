from fastapi import FastAPI

app = FastAPI(title="My Toolbox")

@app.get("/")
def root():
    return {"message":"hello toolbox"}

@app.get("/health")
def health():
    return {"status":"ok"}