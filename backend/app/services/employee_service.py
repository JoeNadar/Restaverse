# Service: business rules. Decides what is allowed and what to return.
import math

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import employee_repository


def search_employees(db: Session, search: str | None, page: int, size: int):
    if search is not None:
        search = search.strip()
        if search == "":
            raise HTTPException(status_code=400, detail="Search query cannot be empty")

    total = employee_repository.count_employees(db, search)
    pages = math.ceil(total / size)

    if total > 0 and page > pages:
        raise HTTPException(
            status_code=404,
            detail=f"Page {page} does not exist. Total pages: {pages}",
        )

    skip = (page - 1) * size
    employees = employee_repository.get_employees(db, search, skip, size)

    return {
        "total": total,
        "page": page,
        "size": size,
        "pages": pages,
        "items": employees,
    }
