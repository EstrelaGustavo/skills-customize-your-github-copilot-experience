# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for a small book catalog using FastAPI. Practice defining API routes, validating request data, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Prepare the API

#### Description
Install the required packages and run the provided FastAPI application. Explore the starter code and the interactive API documentation.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn with `pip install fastapi uvicorn`.
- Run the application with `uvicorn starter_code:app --reload`.
- Open `/docs` in a browser and identify the book data fields used by the API.


### 🛠️ Add Read Endpoints

#### Description
Create endpoints that let a client retrieve all books or retrieve one book by its ID.

#### Requirements
Completed program should:

- Implement `GET /books` and return the books as JSON.
- Implement `GET /books/{book_id}` and return the matching book.
- Return HTTP `404` when the requested book ID does not exist.


### 🛠️ Complete Book Management

#### Description
Add endpoints to create, update, and delete books in the in-memory catalog. Use the provided Pydantic model to validate request data.

#### Requirements
Completed program should:

- Implement `POST /books` to create a book and return HTTP `201` with its assigned ID.
- Implement `PUT /books/{book_id}` to update a book, returning HTTP `404` if it does not exist.
- Implement `DELETE /books/{book_id}` to delete a book and return HTTP `204`; return HTTP `404` if it does not exist.
- Test each endpoint in the interactive `/docs` page, including at least one request for a book ID that does not exist.
