
from pydantic import BaseModel
from datetime import datetime

class Member(BaseModel):
    id: int
    parentId: int
    surname: str
    title: str
    first_name: str
    last_name: str
    birth_year: str
    relation_to_head:str
    second_name: str
    fathers_name:str
    mosal:str
    profession:str
    address_line1:str
    address_line2:str
    town:str
    county:str
    post_code:str
    telephone:str
    mobile:str
    email:str
    newsletter:bool = False
    directory:bool = False
    created_at: datetime
    update_at: datetime


class MemberCreateModel(BaseModel):
    parentId: int
    surname: str
    title: str
    first_name: str
    last_name: str
    birth_year: str
    relation_to_head:str
    second_name: str
    fathers_name:str
    mosal:str
    profession:str
    address_line1:str
    address_line2:str
    town:str
    county:str
    post_code:str
    telephone:str
    mobile:str
    email:str
    newsletter:bool = False
    directory:bool = False
