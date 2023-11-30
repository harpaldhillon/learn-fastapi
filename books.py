from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'coding book',
                'description': 'new coding book for beginers',
                'rating': 5
            }
        }



class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'Kubernetes In Action', 'Manning', 'Kubernetes Book', 5),
    Book(2, 'AWS In Action', 'Redhat', 'AWS Book', 4),
    Book(3, 'Ruby Best', 'Ruby Plc', 'Ruby Book', 1),
    Book(4, 'GCP Complete', 'Manning', 'GCP Book', 3),
    Book(5, 'Python for Professionals', 'Redhat', 'Python Book', 4),
    Book(6, 'Linux Everything', 'Linux Foundation', 'Linux Book', 5)
]

@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/books/{name}")
async def get_book_by_name(name: str):
    for book in BOOKS:
        if book.title.casefold() == name.casefold():
            return book
        
@app.post("/books/create_book")
async def create_new_book(book: BookRequest):
    new_book = Book(**book.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book


        