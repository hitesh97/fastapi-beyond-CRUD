
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Member(BaseModel):
    id: int = Field(serialization_alias="Id")
    title: str = Field(serialization_alias="Title")
    surname: str = Field(serialization_alias="Surname")
    first_name: str = Field(serialization_alias="FirstName")
    fathers_name: str = Field(serialization_alias="FathersName")
    relation_to_head: str = Field(serialization_alias="RelationToHead")
    parentId: Optional[int] = Field(serialization_alias="ParentId")
    birth_year: Optional[str] = Field(serialization_alias="BirthYear")
    second_name: Optional[str] = Field(serialization_alias="SecondName")
    mosal: Optional[str] = Field(serialization_alias="Mosal")
    profession: Optional[str] = Field(
        serialization_alias="Profession", default=None)
    address_line1: Optional[str] = Field(
        serialization_alias="AddressLine1", default=None)
    address_line2: Optional[str] = Field(
        serialization_alias="AddressLine2", default=None)
    town: Optional[str] = Field(serialization_alias="Town", default=None)
    county: Optional[str] = Field(serialization_alias="County", default=None)
    post_code: Optional[str] = Field(
        serialization_alias="PostCode", default=None)
    telephone: Optional[str] = Field(
        serialization_alias="Telephone", default=None)
    mobile: Optional[str] = Field(serialization_alias="Mobile", default=None)
    email: Optional[str] = Field(serialization_alias="Email", default=None)
    newsletter: Optional[bool] = Field(
        serialization_alias="Newsletter", default=False)
    directory: Optional[bool] = Field(
        serialization_alias="Directory", default=False)
    created_at: datetime = Field(serialization_alias="CreatedAt", default=datetime.now)
    updated_at: datetime = Field(serialization_alias="UpdatedAt", default=datetime.now)


class MemberCreateUpdateModel(BaseModel):
    title: str = Field(serialization_alias="Title",alias="Title")
    surname: str = Field(serialization_alias="Surname",alias="Surname")
    first_name: str = Field(serialization_alias="FirstName",alias="FirstName")
    fathers_name: str = Field(serialization_alias="FathersName",alias="FathersName")
    relation_to_head: str = Field(serialization_alias="RelationToHead", alias="RelationToHead")
    parentId: Optional[int] = Field(serialization_alias="ParentId", alias="ParentId")
    birth_year: Optional[str] = Field(serialization_alias="BirthYear", alias="BirthYear")
    second_name: Optional[str] = Field(serialization_alias="SecondName",alias="SecondName")
    mosal: Optional[str] = Field(serialization_alias="Mosal", alias="Mosal")
    profession: Optional[str] = Field(
        serialization_alias="Profession", default=None,alias="Profession")
    address_line1: Optional[str] = Field(
        serialization_alias="AddressLine1", default=None)
    address_line2: Optional[str] = Field(
        serialization_alias="AddressLine2", default=None)
    town: Optional[str] = Field(serialization_alias="Town", default=None)
    county: Optional[str] = Field(serialization_alias="County", default=None)
    post_code: Optional[str] = Field(
        serialization_alias="PostCode", default=None)
    telephone: Optional[str] = Field(
        serialization_alias="Telephone", default=None)
    mobile: Optional[str] = Field(serialization_alias="Mobile", default=None)
    email: Optional[str] = Field(serialization_alias="Email", default=None)
    newsletter: Optional[bool] = Field(
        serialization_alias="Newsletter", default=False)
    directory: Optional[bool] = Field(
        serialization_alias="Directory", default=False)
    update_at: datetime = Field(serialization_alias="UpdatedAt", default=datetime.now)
