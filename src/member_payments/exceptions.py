from src.bookly_exception import BooklyException
from fastapi import FastAPI, status

from src.exception_creator import create_exception_handler


class MemberPaymentNotFound(BooklyException):
    """Member Payment Not found"""

    pass

def register_member_payment_errors(app: FastAPI):
    app.add_exception_handler(
        MemberPaymentNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "member payment not found",
                "error_code": "member_payment_not_found",
            },
        ),
    )