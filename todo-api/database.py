from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection URL
DATABASE_URL = "postgresql://postgres:Pt13864$$@localhost/todo_db"

# Engine create (DB connection)
engine = create_engine(DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()