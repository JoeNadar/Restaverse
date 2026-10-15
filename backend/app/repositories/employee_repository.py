# Repository: the only place that talks to the database.
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.database_models import Employee


def _apply_search(query, search):
    if search:
        # "rahul%" means "starts with rahul". This can use the index on
        # name/department, so it stays fast even with lots of employees.
        pattern = f"{search}%"
        query = query.filter(
            or_(
                Employee.name.like(pattern),
                Employee.department.like(pattern),
            )
        )
    return query


def count_employees(db: Session, search: str | None):
    query = _apply_search(db.query(Employee), search)
    return query.count()


def get_employees(db: Session, search: str | None, skip: int, limit: int):
    query = _apply_search(db.query(Employee), search)
    return query.order_by(Employee.id).offset(skip).limit(limit).all()
