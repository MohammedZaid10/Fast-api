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
async def read_all_books():
    return BOOKS

# Always make sure that an API with a static parameter comes before a dynamic parameter
# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book title': 'My favourite book'}


# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):
#     return {'dynamic_param': dynamic_param}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
