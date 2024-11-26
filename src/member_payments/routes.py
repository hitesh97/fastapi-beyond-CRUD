from fastapi import APIRouter, Depends, status

from src.db.main import get_session
from src.member_payments.schemas import MemberPayment, MemberPaymentCreateUpdateModel
from src.members.exceptions import MemberNotFound
from src.members.service import MemberService
from .service import MemberPaymentService
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

member_payment_router = APIRouter()
member_payment_service = MemberPaymentService()
member_service = MemberService()

@member_payment_router.get("/{member_id}", response_model=List[MemberPayment], status_code=status.HTTP_200_OK)
async def get_payments_by_member_id(member_id:int, session: AsyncSession = Depends(get_session)):
    member_payments = await member_payment_service.get_payments_by_member_id(member_id, session)
    
    return member_payments


@member_payment_router.post("/{member_id}", response_model=MemberPayment, status_code=status.HTTP_201_CREATED)
async def create_member_payment(member_id:int, member_payment_data: MemberPaymentCreateUpdateModel, session: AsyncSession = Depends(get_session)):
    existing_member = await member_service.get_member(member_id, session)
    
    if(existing_member == None):
        raise MemberNotFound()
    
    member_payment = await member_payment_service.create_member_payment(member_id, member_payment_data, session)
        
    return member_payment