Fast-API
========

Commands:
to create new venv : python -m venv fastapienv
activate venv : .\fastapienv\Scripts\Activate.ps1
install these : python -m pip install setuptools wheel
install fastapi : pip install fastapi or pip install "fastapi[standard]"
install uvicorn : pip install "uvicorn[standard]"
to run fastapi app : uvicorn books:app --reload or fastapi dev Books.py or fastapi run Books.py

======================================================================

TOPICS In Project 1:

1. CRUD IN Fast-API:
  a. POST request is CREATE
  b. GET request is READ
  c. PUT request is UPDATE:
      We are going to use Body() and assign it to a variable as we want to generate a request body to put our JSON in
  d. DELETE request is DELETE
2. Order of execution
3. Dynamic Paramters :
  a. Path Paramters
  b. Query Parameters

======================================================================

Questions to practise from Project 1:
  Create a new API Endpoint that can fetch all books from a specific author using either Path Parameters or Query Parameters.

======================================================================

Lesson 69 - FastAPI Project - Enhance Get Request

Go to this path to open Swagger UI, to test all API endpoints : http://127.0.0.1:8000/docs

Books.py:

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'Science'},
    {'title': 'Title Tow', 'author': 'Author Two', 'category': 'Science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'History'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'Math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'Math'}
]


@app.get("/books")
async def read_all_books(): // giving async is optional in python
    return BOOKS

======================================================================

Lesson 70 - FastAPI Project: Path Parameters Overview

In FastAPI, the APIs are called from top to bottom, so if two URLs match, then the first will be taken, so always make sure that the APIs are called correctly

Lets say the REQUEST URL is :
http://127.0.0.1:8000/books/title%20four

then this code :
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

will return this response:
{
  'title': 'Title Four', 
  'author': 'Author Four', 
  'category': 'Math'
}

======================================================================

Lesson 71 - FastAPI Project: Path Parameters

Path paramters can be used for dynamic routing as done in below code:
@app.get("/books/{book_title}")

Books.py:

from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'Science'},
    {'title': 'Title Tow', 'author': 'Author Two', 'category': 'Science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'History'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'Math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'Math'}
]


// Always make sure that an API with a static parameter comes before a dynamic parameter
// @app.get("/books/mybook")
// async def read_all_books():
//     return {'book title': 'My favourite book'}


// @app.get("/books/{dynamic_param}")
// async def read_all_books(dynamic_param: str):
//     return {'dynamic_param': dynamic_param}


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

======================================================================

Lesson 72 : FastAPI Project: Query Parameters Overview &
Lesson 73 : FastAPI Project: Query Parameters

Query paramters are used when we want to filter the result based on some data:

@app.get("/books/")
async def read_category_by_books(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

Using Path parameters using Query Parameters:
@app.get("/books/{book_author}/")
async def read_books_by_author_and_category(book_author: str, book_category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == book_category.casefold():
            books_to_return.append(book)
    return books_to_return

======================================================================

Lesson 74 : FastAPI Project: Post Request Overview &
Lesson 75 : FastAPI Project: Post Request 

You wont see the data in create_book url : 
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

curl -X POST "http://127.0.0.1:8000/books/create_book" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"title\": \"Title Eight\", \"author\": \"Author Two\", \"category\": \"Science\"}"

======================================================================

Lesson 76 : FastAPI Project: Put Request Overview &
Lesson 77 : FastAPI Project: Put Request

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            
(or)

@app.put("/books/update_book/")
async def update_book(updated_book_data=Body()):
    title_from_body = updated_book_data.get("title")
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == title_from_body.casefold():
            BOOKS[i] = updated_book_data

(or)

@app.put("/books/update_book/{book_update}/")
async def update_book(book_update: str, updated_book_data=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_update.casefold():
            BOOKS[i] = updated_book_data

======================================================================

Lesson 78 : FastAPI Project: Delete Request Overview
Lesson 79 : FastAPI Project: Delete Request

@app.delete("/books/delete_books/{book_title}")
async def delete_books(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

======================================================================

Lesson 80 & 81 : PROJECT 1 : Assignment

@app.get("/books/author/{book_author}")
async def fetch_books(book_author: str):
    books_to_return = []
    for Book in BOOKS:
        if Book.get("author").casefold() == book_author.casefold():
            books_to_return.append(Book.get("title"))
    return books_to_return

======================================================================

# --- REORDERED ENDPOINTS (GETs first, from Most Specific to Least Specific) ---

# 1. Most specific path with multiple dynamic segments (e.g., /books/AUTHOR_NAME/CATEGORY_NAME/)
# This captures URLs like /books/AuthorOne/Science/
@app.get("/books/{book_author}/{book_category}/")
async def read_books_by_author_and_category(book_author: str, book_category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
                book.get("category").casefold() == book_category.casefold():
            books_to_return.append(book)
    return books_to_return


# 2. Paths with a static segment followed by a dynamic parameter (e.g., /books/author/NAME)
# This captures URLs like /books/author/AuthorOne
@app.get("/books/author/{book_author}")
async def fetch_books(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return


# 3. General path with a single dynamic parameter (e.g., /books/ANY_STRING)
# This captures URLs like /books/TitleOne. It must come after more specific dynamic paths.
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# 4. Root collection path with query parameters (e.g., /books/?category=Science)
# This uses a query parameter, so its order relative to path parameters is less critical,
# but it's fine here after the more specific path parameter routes.
@app.get("/books/")
async def read_category_by_books(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# 5. General collection path (no parameters, e.g., /books)
@app.get("/books")
async def read_all_books():
    return BOOKS


# --- POST (Create) Operations ---
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book


# --- PUT (Update) Operations ---
# This uses a path parameter, so it's fine after the GETs.
@app.put("/books/update_book/{book_update}/")
async def update_book(book_update: str, updated_book_data=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_update.casefold():
            BOOKS[i] = updated_book_data
            break # Stop after finding and updating the first matching book


# --- DELETE Operations ---
# This uses a path parameter, so it's fine after the GETs.
@app.delete("/books/delete_books/{book_title}")
async def delete_books(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

======================================================================