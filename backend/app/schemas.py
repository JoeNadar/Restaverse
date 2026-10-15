from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    department: str
    designation: str
    date_of_joining: date


class PaginatedEmployees(BaseModel):
    total: int
    page: int
    size: int
    pages: int
    items: list[EmployeeResponse]
