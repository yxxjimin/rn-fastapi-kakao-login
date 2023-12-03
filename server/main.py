from fastapi import FastAPI
from pydantic import BaseModel


class Login(BaseModel):
    id: int = None
    connected_at: str = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login/")
async def login(login: Login):
    print(login.id)
    return f"user-{str(login.id)}"