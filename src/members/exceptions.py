from src.bookly_exception import BooklyException
from fastapi import FastAPI, status

from src.exception_creator import create_exception_handler


class MemberNotFound(BooklyException):
    """User Not found"""

    pass

def register_member_errors(app: FastAPI):
    app.add_exception_handler(
        MemberNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "member not found",
                "error_code": "member_not_found",
            },
        ),
    )