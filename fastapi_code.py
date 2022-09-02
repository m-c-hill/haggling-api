import uvicorn
from fastapi import FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    message: str

settings = Settings()
app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "GdET"}

@app.post("/")
def home_post():
    return {"Hello": "POST"}

@app.get("/employee")
def home(department: str):
    return {"department": department}

if __name__ == "__main__":
    uvicorn.run("fastapi_code:app", reload=True)
