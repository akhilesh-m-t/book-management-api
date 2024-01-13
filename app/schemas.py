from pydantic import BaseModel, Field


class Create_User(BaseModel):
    user_name: str
    full_name: str
    user_email: str
    password: str = Field(min_length=8, max_length=30)
    is_active: bool = True


class Login_User(BaseModel):
    user_email: str
    password: str = Field(min_length=8, max_length=30)


class Response_User(BaseModel):
    id: int
    user_name: str
    full_name: str
    user_email: str
    is_active: bool


class Create_Book(BaseModel):
    book_name: str
    category_name: str | None = None
    book_author: str | None = None
    is_favourite: bool = False
    user_id: int


class Response_Book(Create_Book):
    category_name: str
    book_author: str
    is_favourite: bool
