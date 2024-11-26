
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class MemberPayment(BaseModel):
    id: int
    member_id: Optional[int] =  None
    year: Optional[int] =  None
    receipt_no: Optional[str] =  None
    amount: Optional[float] = None
    is_cheque: Optional[bool] = None
    cheque_no: Optional[str] = None
    is_donation: Optional[bool] = None
    created_at: datetime
    update_at: datetime


class MemberPaymentCreateUpdateModel(BaseModel):
    year: Optional[int] =  None
    receipt_no: Optional[str] =  None
    amount: Optional[float] = None
    is_cheque: Optional[bool] = Field(default=False)
    cheque_no: Optional[str] = None
    is_donation: Optional[bool] =  Field(default=False)