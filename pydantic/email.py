from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr


user = User(email="abc")

print(user)
