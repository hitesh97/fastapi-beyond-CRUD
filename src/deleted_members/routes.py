
from fastapi import APIRouter, Depends, status

from src.db.main import get_session
# from .exceptions import MemberNotFound
from .schemas import DeletedMember, DeletedMemberCreateUpdateModel

from .service import DeletedMemberService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.members.service import MemberService
from src.members.exceptions import MemberNotFound

deleted_member_router = APIRouter()
deleted_member_service = DeletedMemberService()
member_service = MemberService()

@deleted_member_router.get("/", response_model=List[DeletedMember], status_code=status.HTTP_200_OK)
async def get_all_members(session: AsyncSession = Depends(get_session)):
    members = await deleted_member_service.get_all_deleted_members(session)
    return members

@deleted_member_router.post("/{member_id}", response_model=DeletedMember, status_code=status.HTTP_201_CREATED)
async def create_deleted_member(member_id: int, deleted_reason:str, session: AsyncSession = Depends(get_session)):
    
    member_payment = await deleted_member_service.create_deleted_member(member_id, deleted_reason, session)
        
    return member_payment