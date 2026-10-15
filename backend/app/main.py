from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware

from app import database_models  
from app.core.config import settings
from app.core.database import Base, engine
from app.routers import employee_router

app = FastAPI(title="Employee API")

app.add_middleware(
    CORSMiddleware,
    # e.g. "http://localhost:5173,http://127.0.0.1:5173" -> list of URLs
    allow_origins=[origin.strip() for origin in settings.FRONTEND_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# this will create table if it does not exists
try:
    Base.metadata.create_all(bind=engine)
except OperationalError:
    print("Could not connect to the database. Tables were not created.")

app.include_router(employee_router.router)


# Database is down / wrong credentials -> 503
@app.exception_handler(OperationalError)
def database_down_handler(request: Request, exc: OperationalError):
    print(f"Database connection error: {exc}")
    return JSONResponse(
        status_code=503,
        content={"detail": "Database is not available. Please try again later."},
    )


# Any other database error -> 500 (don't show SQL details to the user)
@app.exception_handler(SQLAlchemyError)
def database_error_handler(request: Request, exc: SQLAlchemyError):
    print(f"Database error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Something went wrong with the database."},
    )
