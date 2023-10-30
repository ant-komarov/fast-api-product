from sqlalchemy.orm import Session

from db.database import SessionLocal


def get_db() -> Session:
    with SessionLocal() as session:
        yield session
