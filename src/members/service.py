from src.db.models import Member
from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.members.schemas import MemberCreateUpdateModel


class MemberService:
    async def get_all_head_members(self, session: AsyncSession):
        statement = select(Member).where(Member.parentId == -1) .order_by(desc(Member.created_at))
        result = await session.exec(statement)
        
        return result.all()

    async def get_all_members(self, session: AsyncSession):
        statement = select(Member).order_by(desc(Member.created_at))
        result = await session.exec(statement)
        
        return result.all()
    
    async def get_member(self, member_id:int, session: AsyncSession):
        statement = select(Member).where(Member.id == member_id)
        result = await session.exec(statement)
        
        member = result.first()
        
        return member if member is not None else None
    
    async def create_member(self, member_data: MemberCreateUpdateModel, session: AsyncSession):
        new_member = Member(**member_data.model_dump(exclude_unset=True))
                
        session.add(new_member)
        await session.commit()
        return new_member
    
    async def update_member(self,  member_id:int, member_data: MemberCreateUpdateModel, session: AsyncSession):
        member_to_update = await self.get_member(member_id, session)
        
        if(member_to_update is None):
            return None
        
        member_data_dict = member_data.model_dump(exclude_unset=True)

        for k, v in member_data_dict.items():
            setattr(member_to_update, k, v)
        
        await session.commit()

        member_to_update = await self.get_member(member_id, session)
        return member_to_update
    
    async def delete_member(self, member_id:int, session: AsyncSession):
        member_to_delete = await self.get_member(member_id, session)

        if(member_to_delete is None):
            return None

        await session.delete(member_to_delete)
        await session.commit()

        return {}
    