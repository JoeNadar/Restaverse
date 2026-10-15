# Router: only receives the request and passes it to the service.
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas import PaginatedEmployees
from app.services import employee_service

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("", response_model=PaginatedEmployees)
def get_employees(
    search: Optional[str] = Query(None, max_length=100),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return employee_service.search_employees(db, search, page, size)
