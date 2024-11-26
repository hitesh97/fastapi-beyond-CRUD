
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class DeletedMember(BaseModel):
    id: int
    member_id: int
    title: str
    surname: str
    first_name: str
    fathers_name: str
    relation_to_head: str
    parentId: Optional[int]=  None
    birth_year: Optional[str] =  None
    second_name: Optional[str]=  None
    mosal:Optional[str]=  None
    profession:Optional[str]=  None
    address_line1:Optional[str]=  None
    address_line2:Optional[str]=  None
    town:Optional[str]=  None
    county:Optional[str]=  None
    post_code:Optional[str]= None
    telephone:Optional[str]=  None
    mobile:Optional[str]=  None
    email:Optional[str]=  None
    newsletter:Optional[bool] = False
    directory:Optional[bool] = False
    deleted_reason:Optional[str]=  None
    created_at: datetime
    update_at: datetime


class DeletedMemberCreateUpdateModel(BaseModel):
    member_id: int
    parentId: Optional[int]= None
    title: Optional[str]= None
    surname: Optional[str]= None
    first_name: Optional[str]= None
    birth_year: Optional[str]= None
    relation_to_head:Optional[str]= None
    second_name: Optional[str]= None
    fathers_name:Optional[str]=  None
    mosal:Optional[str]=  None
    profession:Optional[str]=  None
    address_line1:Optional[str]=  None
    address_line2:Optional[str]= None
    town:Optional[str]=  None
    county:Optional[str]= None
    post_code:Optional[str]= None
    telephone:Optional[str]= None
    mobile:Optional[str]= None
    email:Optional[str]=  None
    newsletter:Optional[bool] = False
    directory:Optional[bool] = False
    deleted_reason:str
