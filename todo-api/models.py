from sqlalchemy import Column, Integer, String
from database import Base

# Table definition
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task = Column(String, index=True)