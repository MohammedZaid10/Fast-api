Fast-API
========

Pydantic v1 vs Pydantic v2
FastAPI is now compatible with both Pydantic v1 and Pydantic v2.

Based on how new the version of FastAPI you are using, there could be small method name changes.

The three biggest are:

.dict() function is now renamed to .model_dump()

schema_extra function within a Config class is now renamed to json_schema_extra

Optional variables need a =None example: id: Optional[int] = None

======================================================================

Lesson 86 : FastAPI Project: Pydantics and Data Validation Overview

Syntax for Pydantic data validation which is done by calling "BaseModel" in our constructor class which is the pydantic model:

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=5)

    @app.post("/create-book")
    async def create_book(book_request: BookRequest):
        new_book = Book(**book_request.dict())
        BOOKS.append(new_book)

** operator will pass the key/value from BookRequest() into the Book() constructor

======================================================================

Lesson 87 : FastAPI Project: Pydantic Book request Validation

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOKS.append(book_request)

======================================================================

Lesson 88 : FastAPI Project: Fields - Data Validation