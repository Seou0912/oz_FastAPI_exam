from fastapi import APIRouter
import crud
import schemas
from sqlalchemy.orm import Session
import dependencies
from typing import Depends

router = APIRouter()

@router.post('/')
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db))
    db_user = crud.create_user(db, user)
    return db_user

