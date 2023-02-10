from sqlmodel import SQLModel, Field
from typing import Optional


class Book(SQLModel, table=True):
    __tablename__ = "book"
    id: Optional[int] = Field(primary_key=True, nullable=False)
    title: str
    price: int
