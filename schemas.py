from pydantic import BaseModel, List


class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class User(BaseModel):
    id: int
    email: str

    items: List[Item]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    email: str | None = None
    password: str | None = None  # python 3.10   부터 추가된 기능.
