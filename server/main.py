from fastapi import FastAPI
from pydantic import BaseModel
from db import EngineConnection
from models import User
import httpx

# App
app = FastAPI()

# Database connection
engine = EngineConnection()
session = engine.sessionmaker()

@app.get("/")
def read_root():
    return {"Hello": "World"}


class AccessRequest(BaseModel):
    access_token: str


async def getKakaoUser(access_token):
    """
    Fetch user information from Kakao API.

    Args:
        access_token (str): Used for Bearer token authorization.

    Returns:
        res (dict): Given as {'id': (int), 'connected_at': (str)}
    """
    async with httpx.AsyncClient() as client:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        kakao_url = 'https://kapi.kakao.com/v2/user/me'
        res = await client.get(kakao_url, headers=headers)
        res = res.json()

        return res

@app.post("/login/")
async def login(request_body: AccessRequest):
    access_token = request_body.access_token
    fetched_user = await getKakaoUser(access_token)
    
    user = session.query(User).get(fetched_user['id'])
    
    # If user ID is not in database, register user
    if user is None:
        user = User(id=fetched_user['id'],
                    name=f"user-{str(fetched_user['id'])}",
                    connected_at=fetched_user['connected_at'])
        session.add(user)
        session.commit()

    return user.name