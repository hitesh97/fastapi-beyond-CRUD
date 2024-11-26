from fastapi import FastAPI
from src.auth.routes import auth_router
from src.books.routes import book_router
from src.member_payments.exceptions import register_member_payment_errors
from src.members.exceptions import register_member_errors
from src.reviews.routes import review_router
from src.tags.routes import tags_router
from src.members.routes import member_router
from src.member_payments.routes import member_payment_router

from src.deleted_members.routes import deleted_member_router
from .errors import register_all_errors
from .middleware import register_middleware


version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix =f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description=description,
    version=version,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Ssali Jonathan",
        "url": "https://github.com/jod35",
        "email": "ssalijonathank@gmail.com",
    },
    terms_of_service="httpS://example.com/tos",
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc"
)

register_all_errors(app)
register_member_errors(app)
register_member_payment_errors(app)

register_middleware(app)


app.include_router(book_router, prefix=f"{version_prefix}/books", tags=["books"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"{version_prefix}/reviews", tags=["reviews"])
app.include_router(tags_router, prefix=f"{version_prefix}/tags", tags=["tags"])
app.include_router(member_router, prefix=f"{version_prefix}/members", tags=["members"])
app.include_router(member_payment_router, prefix=f"{version_prefix}/member/payments", tags=["member_payments"])

app.include_router(deleted_member_router, prefix=f"{version_prefix}/member/deleted", tags=["deleted_members"])