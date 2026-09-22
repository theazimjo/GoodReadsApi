from sqlalchemy import Column, Integer, VARCHAR, TEXT, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship

from database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR, unique=True)
    email = Column(VARCHAR, unique=True)
    password_hash = Column(VARCHAR)
    bio = Column(TEXT)
    avatar_url = Column(VARCHAR)
    created_at = Column(TIMESTAMP)
    user_books = relationship("UserBooks", back_populates="Users")


class UserBooks(Base):
    __tablename__ = "user_books"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey="users.id")
    book_id = Column(Integer)
    status = Column(Enum)
    created_at = Column(TIMESTAMP)
    users = relationship("Users", back_populates="UserBooks")
