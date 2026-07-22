import random
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import UserCreate, MixRequest
from app.config import settings

app = FastAPI(title="service2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/register")
def register_user(payload: UserCreate):
    try:
        with open("users_data.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {payload.name}, Age: {payload.age}\n")
        return {"status": "ok", "message": "Успешная регистрация"}
    except Exception:
        raise HTTPException(status_code=500, detail="Ошибка записи на сервере")

@app.post("/api/mix")
def mix_characters(payload: MixRequest):
    if not payload.text:
        return {"result": ""}
    
    char_list = list(payload.text)
    random.shuffle(char_list)
    mixed_text = "".join(char_list)
    
    return {"result": mixed_text}
