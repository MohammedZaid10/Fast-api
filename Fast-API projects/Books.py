from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"}
]


@app.get("/books/author/{book_author}")
async def fetch_books(book_author: str):
    books_to_return = []
    for Book in BOOKS:
        if Book.get("author").casefold() == book_author.casefold():
            books_to_return.append(Book.get("title"))
    return books_to_return


@app.get("/books")
async def read_all_books():
    return BOOKS

# Always make sure that an API with a static parameter comes before a dynamic parameter
# @app.get("/books/mybook")
# async def read_all_books():
#     return {"book title": "My favourite book"}


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):
#     return {"dynamic_param": dynamic_param}


@app.get("/books/")
async def read_category_by_books(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_books_by_author_and_category(book_author: str, book_category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and \
                book.get("category").casefold() == book_category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book


# @app.put("/books/update_book/")
# async def update_book(updated_book_data=Body()):
#     title_from_body = updated_book_data.get("title")
#     for i in range(len(BOOKS)):
#         if BOOKS[i].get("title").casefold() == title_from_body.casefold():
#             BOOKS[i] = updated_book_data

@app.put("/books/update_book/{book_update}/")
async def update_book(book_update: str, updated_book_data=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_update.casefold():
            BOOKS[i] = updated_book_data


@app.delete("/books/delete_books/{book_title}")
async def delete_books(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


@app.get("/books/author/{book_author}")
async def fetch_books(book_author: str):
    books_to_return = []
    for Book in BOOKS:
        if Book.get("author").casefold() == book_author.casefold():
            books_to_return.append(Book)


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
