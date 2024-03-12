from fastapi import APIRouter, HTTPException
from models import Movie


route = APIRouter()

# Movie 데이터를 저장할 리스트
movie_db = [
    {
        "id": 1,
        "name": "Star Wars: Episode IX - The Rise of Skywalker",
        "plot": "The surviving members of the resistance face the First Order once again.",
        "genres": ["Action", "Adventure", "Fantasy"],
        "casts": ["Daisy Ridley", "Adam Driver"],
    }
]


@route.get("/")
def read_movies():
    return movie_db


@route.post("/")
def add_movie(movie: Movie):
    new_movie = movie.dict()
    new_movie["id"] = len(movie_db) + 1
    movie_db.append(new_movie)
    return new_movie


@route.put("/{id}")
def update_movie(id: int, movie: Movie):
    for movie_item in movie_db:
        if movie_item["id"] == id:
            movie_item.update(movie.dict())
            return movie_item
    raise HTTPException(status_code=404, detail="Movie not found")


@route.delete("/{id}")
def delete_movie(id: int):
    for movie_item in movie_db:
        if movie_item["id"] == id:
            movie_db.remove(movie_item)
            return {"message": "Movie has been deleted successfully"}
    raise HTTPException(status_code=404, detail="Movie not found")
