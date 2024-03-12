from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    hashed_password = Column(String)

    items = relationship("Item", back_populates="owner")


# CREATE TABLE users(
# id INT PRIMARY KEY AUTO_INCREMENT,
# email VARCHAR(255),
# HASHED_PASSWORD VARCHAR(255)
# )


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, Foreignkey("users.id"))

    owner = relationship("User", back_populates="items")
