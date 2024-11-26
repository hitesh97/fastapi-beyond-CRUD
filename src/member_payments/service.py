from src.db.models import MemberPaymentInfo
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.member_payments.schemas import MemberPaymentCreateUpdateModel
from src.members.service import MemberService

member_service = MemberService()

class MemberPaymentService:
    async def get_payments_by_member_id(self, member_id:int, session: AsyncSession):
        statement = select(MemberPaymentInfo).where(MemberPaymentInfo.member_id == member_id)
        result = await session.exec(statement)
        return result.all()
    
    async def create_member_payment(self, member_id: int, member_payment_data: MemberPaymentCreateUpdateModel, session: AsyncSession):
        
        new_member_payment = MemberPaymentInfo(**member_payment_data.model_dump(exclude_unset=True))
        new_member_payment.member_id = member_id
        session.add(new_member_payment)
        await session.commit()
        return new_member_payment