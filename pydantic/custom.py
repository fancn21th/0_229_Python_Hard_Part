from pydantic import (
    BaseModel,
    field_validator,
)


class User(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, v: str) -> str:
        if " " not in v:
            raise ValueError("must contain a space")
        return v.title()


user = User(name="samuelcolvin")

print(user)
