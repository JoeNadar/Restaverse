from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

# The engine keeps a pool of open connections and reuses them,
# instead of opening a new connection for every request.
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,         # keep up to 10 connections open
    max_overflow=20,      # allow 20 extra connections when traffic is high
    pool_recycle=1800,    # refresh connections every 30 min (MySQL closes idle ones)
    pool_pre_ping=True,   # check a connection is alive before using it
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Gives each request its own session and always closes it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
