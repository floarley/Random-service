from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    name: str
    age: int

    @field_validator('age')
    @classmethod
    def check_age(cls, value: int) -> int:
        if value < 18:
            raise ValueError('Доступ только для совершеннолетних')
        return value

class MixRequest(BaseModel):
    text: str
