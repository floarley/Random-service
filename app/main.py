import random
import string
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import UserCreate
from app.config import settings

app = FastAPI(title="Soulmate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/user")
async def save_user(payload: UserCreate):
    # TODO: переписать на СУБД, пока пишем в лог-файл
    with open("users_data.txt", "a", encoding="utf-8") as f:
        f.write(f"{payload.name} | {payload.age}\n")
    return {"status": "ok"}

@app.get("/api/soulmate")
async def get_soulmate(nickname: str):
    length = random.randint(5, 10)
    chars = string.ascii_lowercase
    soulmate_name = "".join(random.choices(chars, k=length))
    return {"soulmate": soulmate_name}
