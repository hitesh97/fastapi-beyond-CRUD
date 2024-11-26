from src.db.models import DeletedMember
from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.members.service import MemberService

member_service = MemberService()
class DeletedMemberService:
    async def get_all_deleted_members(self, session: AsyncSession):
        statement = select(DeletedMember).order_by(desc(DeletedMember.created_at))
        result = await session.exec(statement)
        
        return result.all()
    
    async def create_deleted_member(self, member_id: int, deleted_reason:str, session: AsyncSession):
        existing_member = await member_service.get_member(member_id, session)
        
        if(existing_member == None):
            return None
        
        # print(schema_member)
        # TODO: find a way to create a new member from the existing one in easy way!!
        new_deleted_member = DeletedMember(
            member_id = member_id,
            parentId= existing_member.parentId,
            title= existing_member.title,
            first_name= existing_member.first_name,
            surname= existing_member.surname,
            birth_year= existing_member.birth_year,
            relation_to_head= existing_member.relation_to_head,
            second_name= existing_member.second_name,
            fathers_name= existing_member.fathers_name,
            mosal= existing_member.mosal,
            profession= existing_member.profession,
            address_line1= existing_member.address_line1,
            address_line2= existing_member.address_line2,
            town= existing_member.town,
            county= existing_member.county,
            post_code= existing_member.post_code,
            telephone= existing_member.telephone,
            mobile= existing_member.mobile,
            email= existing_member.email,
            newsletter= existing_member.newsletter,
            directory= existing_member.directory,
            is_discontinued= existing_member.is_discontinued,
            deleted_reason=deleted_reason
        )

        session.add(new_deleted_member)
        
        deleted_member = await member_service.delete_member(new_deleted_member.member_id, session)
        
        if(deleted_member == None):
            await session.rollback()
            return None
    
        await session.commit()
        return new_deleted_member