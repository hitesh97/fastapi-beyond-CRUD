
from fastapi import APIRouter, Depends, status

from src.db.main import get_session
from .exceptions import MemberNotFound
from .schemas import Member, MemberCreateUpdateModel

from .service import MemberService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

member_router = APIRouter()
member_service = MemberService()

@member_router.get("", response_model=List[Member], status_code=status.HTTP_200_OK)
async def get_all_members(session: AsyncSession = Depends(get_session)):
    members = await member_service.get_all_members(session)
    return members

@member_router.get("/heads", response_model=List[Member], status_code=status.HTTP_200_OK)
async def get_all_head_members(session: AsyncSession = Depends(get_session)):
    members = await member_service.get_all_head_members(session)
    return members

@member_router.get("/{member_id}", response_model=Member, status_code=status.HTTP_200_OK)
async def get_member_by_id(member_id:int, session: AsyncSession = Depends(get_session)):
    member = await member_service.get_member(member_id, session)
    
    if not member:
        raise MemberNotFound()
    
    return member

@member_router.post("", response_model=Member, status_code=status.HTTP_201_CREATED)
async def create_member(member_data: MemberCreateUpdateModel, session: AsyncSession = Depends(get_session)):
    new_member = await member_service.create_member(member_data, session)
    return new_member

@member_router.patch("/{member_id}", response_model=Member, status_code=status.HTTP_202_ACCEPTED)
async def update_member(member_id:int, member_data: MemberCreateUpdateModel, session: AsyncSession = Depends(get_session)):
    updated_member = await member_service.update_member(member_id, member_data, session)
    
    if not updated_member:
        raise MemberNotFound()
    
    return updated_member

@member_router.delete("/{member_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_member(member_id:int, session: AsyncSession = Depends(get_session)):
    deleted_member = await member_service.delete_member(member_id, session)
    
    if deleted_member is None:
        raise MemberNotFound()
    
    return deleted_member
