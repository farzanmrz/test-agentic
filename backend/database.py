from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from backend.config import settings


def build_db_url():
    user = settings.DB_USER
    password = settings.DB_PASSWORD
    host = settings.DB_HOST
    port = settings.DB_PORT
    db = settings.DB_NAME
    # If password is blank, omit the colon and password
    if password:
        return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    else:
        return f"postgresql+psycopg2://{user}@{host}:{port}/{db}"


SQLALCHEMY_DATABASE_URL = build_db_url()

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
