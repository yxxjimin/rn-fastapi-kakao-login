from fastapi import FastAPI
from pydantic import BaseModel
from db import EngineConnection
from models import User


class LoginRequest(BaseModel):
    id: int
    connected_at: str

# App
app = FastAPI()

# Database connection
engine = EngineConnection()
session = engine.sessionmaker()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login/")
async def login(request_body: LoginRequest):
    search_user = session.query(User).get(request_body.id)
    # If not registered, add to User
    if search_user is None:
        search_user = User(id=request_body.id, 
                        name=f"user-{str(request_body.id)}")
        session.add(search_user)
        session.commit()
        print("Registered new user: " + search_user.name)
    # Log in user
    else:
        print("Logged in user: " + search_user.name)

    return search_user.name
