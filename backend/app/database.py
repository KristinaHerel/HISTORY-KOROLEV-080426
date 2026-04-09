from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

# PostgreSQL (recommended). Override via env var DATABASE_URL.
# Example:
# postgresql+psycopg2://USER:PASSWORD@HOST:5432/DBNAME
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL не задана! Проверь файл .env")

engine_kwargs = {"echo": False}
if DATABASE_URL.startswith("sqlite"):
    # Needed only for SQLite
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, **engine_kwargs)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()