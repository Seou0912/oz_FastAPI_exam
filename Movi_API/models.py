from typing import List
from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    name: str
    plot: str
    genres: List[str]
    casts: List[str]
