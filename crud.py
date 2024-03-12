from models import User
from schemas import UserCreate
from sqlalchemy.orm import Session
import bcrypt
from typing import List, Optional


# create user
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf8"), bcrypt.gensalt())

    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user


# Read (사용자 정보 조회)
def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


# Update (사용자 정보 업데이트)
def update_user(
    db: Session,
    user_id: int,
    email: Optional[str] = None,
    password: Optional[str] = None,
):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    if email is not None:
        db_user.email = email
    if password is not None:
        hashed_password = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
        db_user.hashed_password = hashed_password

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Delete (사용자 삭제)
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user


# ----------------------------------------------------------------

from models import User
from sqlalchemy.orm import Session
from schemas import UserCreate, UserUpdate
import bcrypt


def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf8"), bcrypt.gensalt())
    db_user = User(email=user.email, hashed_password=hashed_password)

    db.add(db_user)
    db.commit()
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    # db_user.email = user.email
    # db.commit()
    if not db_user:
        return None
    user_data = user.dict()
    for key, value in user_data:
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user
