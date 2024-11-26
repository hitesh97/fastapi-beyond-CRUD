import uuid
from datetime import date, datetime
from typing import List, Optional

import sqlalchemy.dialects.postgresql as pg

# import sqlalchemy.dialects.mssql as mssql
from sqlmodel import Column, Field, Relationship, SQLModel

class MemberPaymentInfo(SQLModel, table=True):
    __tablename__ = "member_payments"
    id: int | None  = Field(
        sa_column=Column(pg.BIGINT,default=None, primary_key=True, autoincrement=True)
    )
    member_id: int | None  = Field(
        sa_column=Column(pg.BIGINT, nullable=False)
    )
    year: int | None = Field(
        sa_column=Column(pg.INTEGER, nullable=False)
    )
    receipt_no: str | None = Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    amount: float | None = Field(
        sa_column=Column(pg.FLOAT, nullable=True, default=0.0)
    )
    is_cheque: bool = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False)
    )
    cheque_no: str | None = Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    is_donation: bool = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False)
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<MemberPayment id:{self.id} member_id:{self.member_id}>"

class DeletedMember(SQLModel, table=True):
    __tablename__ = "deleted_members"
    id: int | None  = Field(
        sa_column=Column(pg.BIGINT,default=None, primary_key=True, autoincrement=True)
    )
    member_id: int | None  = Field(
        sa_column=Column(pg.BIGINT, nullable=False)
    )
    parentId: int | None = Field(
        sa_column=Column(pg.BIGINT, nullable=True)
    )
    title: str | None = Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    first_name: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    surname: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    birth_year: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    relation_to_head:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    second_name: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    fathers_name:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    mosal:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    profession:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    address_line1:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    address_line2:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    town:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    county:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    post_code:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    telephone:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    mobile:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    email:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    newsletter:bool | None = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False)
    )
    directory:bool | None = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False)
    )
    deleted_reason:str | None = Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<DeletedMember {self.first_name} {self.surname}>"

class Member(SQLModel, table=True):
    __tablename__ = "members"
    id: int | None  = Field(
        sa_column=Column(pg.BIGINT,default=None, primary_key=True, autoincrement=True)
    )
    parentId: int | None = Field(
        sa_column=Column(pg.BIGINT, nullable=True)
    )
    title: str | None = Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    first_name: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    surname: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    birth_year: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    relation_to_head:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    second_name: str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    fathers_name:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    mosal:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    profession:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    address_line1:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    address_line2:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    town:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    county:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    post_code:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    telephone:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    mobile:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    email:str | None= Field(
        sa_column=Column(pg.VARCHAR, nullable=True)
    )
    newsletter:bool | None = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False)
    )
    directory:bool | None = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False)
    )
    is_discontinued: bool = Field(
        sa_column=Column(pg.BOOLEAN, nullable=False, default=False, server_default="false")
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<Member {self.first_name} {self.surname}>"

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    username: str
    email: str
    first_name: str
    last_name: str
    role: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False, server_default="user")
    )
    is_verified: bool = Field(default=False)
    password_hash: str = Field(
        sa_column=Column(pg.VARCHAR, nullable=False), exclude=True
    )
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: List["Book"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )
    reviews: List["Review"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}
    )

    def __repr__(self):
        return f"<User {self.username}>"


class BookTag(SQLModel, table=True):
    book_id: uuid.UUID = Field(default=None, foreign_key="books.uid", primary_key=True)
    tag_id: uuid.UUID = Field(default=None, foreign_key="tags.uid", primary_key=True)


class Tag(SQLModel, table=True):
    __tablename__ = "tags"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    name: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: List["Book"] = Relationship(
        link_model=BookTag,
        back_populates="tags",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    def __repr__(self) -> str:
        return f"<Tag {self.name}>"


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="users.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    user: Optional[User] = Relationship(back_populates="books")
    reviews: List["Review"] = Relationship(
        back_populates="book", sa_relationship_kwargs={"lazy": "selectin"}
    )
    tags: List[Tag] = Relationship(
        link_model=BookTag,
        back_populates="books",
        sa_relationship_kwargs={"lazy": "selectin"},
    )

    def __repr__(self):
        return f"<Book {self.title}>"


class Review(SQLModel, table=True):
    __tablename__ = "reviews"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    rating: int = Field(lt=5)
    review_text: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    user_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="users.uid")
    book_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="books.uid")
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    user: Optional[User] = Relationship(back_populates="reviews")
    book: Optional[Book] = Relationship(back_populates="reviews")

    def __repr__(self):
        return f"<Review for book {self.book_uid} by user {self.user_uid}>"
