from database import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.orm import relationship


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False, unique=True)
    user_email = Column(String(200), nullable=False, unique=True)
    full_name = Column(String(100), nullable=False, unique=False)
    hashed_password = Column(String(500), nullable=False)
    is_active = Column(Boolean, nullable=False)
    favorite_books = relationship('Books', back_populates='user')


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String(100), nullable=False)
    book_author = Column(String(100), nullable=False,
                         server_default='Author not mentioned.')
    category_name = Column(String(200), nullable=False,
                           server_default='Category is not mentioned!')
    is_favourite = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates='favorite_books')
