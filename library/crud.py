from datetime import datetime
from sqlalchemy import or_, not_, and_
from .models import Author, Book, Student
from .db import get_db



def create_author(name: str, bio: str = None) -> Author:
    author = Author(name=name, bio=bio)

    with get_db() as session:
        session.add(author)
        session.commit()
        session.refresh(author)

    return author

def get_author_by_id(author_id: int) -> Author | None:
    with get_db() as session:
        author = session.query(Author).filter(Author.id == author_id).first()
    return author


def get_one_author(author_id: int) -> Author | None:
    with get_db() as session:
        author = session.query(Author).get(author_id)
    
    return author


def get_all_authors() -> list[Author]:
    with get_db() as session:
        authors = session.query(Author).all()
    
    return authors


def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
     with get_db() as session:
        author = session.get(Author, author_id)
        if not author:
            return None
        
        if name is not None:
            author.name = name
        if bio is not None:
            author.bio = bio

        session.commit()
     return Author    

def delete_author(author_id: int) -> bool:
    with get_db() as session:
        author = session.get(Author, author_id)
        if not author:
            return False  
        
        if hasattr(author, "books") and author.books:  
            return False
        
        session.delete(author)
        session.commit()
        return True
    

def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    with get_db() as session:
        author = session.get(Author, author_id)
        if not author:
            raise ValueError(f"{author_id} bunday id da muallif chiqmadi")
        
        new_book = Book(
            title=title,
            author_id=author_id,
            published_year=published_year,
            isbn=isbn
        )
        session.add(new_book)
        session.commit()

    return new_book


def get_book_by_id(book_id: int) -> Book | None:
    with get_db() as session:
        book = session.query(Book).filter(Book.id == book_id).first()
    return book


def get_all_books() -> list[Book]:
    with get_db() as session:
        books = session.query(Book).all()
    
    return books


def search_books_by_title(title: str) -> list[Book]:
    with get_db() as session:
        books = session.query(Book).filter(
            or_(Book.title.like(f'%{title}%'), Book.title.like(f'%{title}%'))
        ).all()
    
    return books


def delete_book(book_id: int) -> bool:
     book = get_book_by_id(book_id)

     if book:
        with get_db() as session:
            session.delete(book)
            session.commit()


def create_student(full_name: str, email: str, grade: str = None) -> Student:
    student = Student(
        full_name=full_name,
        email=email,
        grade=grade,
    )
    
    with get_db() as session:
        session.add(student)
        session.commit()


def get_student_by_id(student_id: int) -> Student | None:
    with get_db() as session:
        student = session.query(Student).get(student_id)
    
    return student


def get_all_students() -> list[Student]:
    with get_db() as session:
        students = session.query(Student).all()
    
    return students


def update_student_grade(student_id: int, grade: str) -> Student | None:
    student = get_student_by_id(student_id)

    if student:
        with get_db() as session:
            student.grade = grade if grade else student.grade

            session.add(student)
            session.commit()


