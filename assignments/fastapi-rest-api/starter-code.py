from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookInput(BaseModel):
    title: str
    author: str


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]
next_book_id = 3


@app.get("/books")
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the matching book or raise HTTPException with status 404.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    # TODO: Create a book with next_book_id, store it, and return it.
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book_input: BookInput):
    # TODO: Update the matching book or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Delete the matching book or raise HTTPException with status 404.
    pass
