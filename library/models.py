from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from .db import Base

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(100), nullable=False)
    bio = Column('bio', Text, nullable=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    author_id = Column('author_id',Integer, ForeignKey('authors.id'))
    published_year = Column('published_year',Integer)
    isbn = Column('isbn', String(13), unique=True, nullable=True)
    is_available = Column('is_available', Boolean, default=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
    

    author = relationship('Author', back_populates='books')
    borrows = relationship('Borrow', back_populates='book')


class Student(Base):
    __tablename__ = 'students'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    full_name = Column('full_name', String(150), nullable=False)
    email = Column('email', String(100), unique=True, nullable=False)
    grade = Column('grade', String(20), nullable=True)
    registered_at = Column('registered_at', DateTime, default=datetime.now)
    
    borrows = relationship('Borrow', back_populates='student')

class Borrow(Base):
    __tablename__ = 'borrows'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    book_id = Column('book_id', Integer, ForeignKey('books.id'))
    borrowed_at = Column('borrowed_at', DateTime, default=datetime.now)
    due_date = Column('due_date', DateTime, default=lambda: datetime.now() )
    returned_at = Column('returned_at', DateTime, nullable=True)
    
    student = relationship('Student', back_populates='borrows')
    book = relationship('Book', back_populates='borrows')