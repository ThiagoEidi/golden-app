from pydantic import BaseModel, EmailStr


# Schemas Users
class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    senha: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
