from sqlalchemy import Column, TEXT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(BIGINT, nullable=False, primary_key=True)
    name = Column(TEXT, nullable=True)
    connected_at = Column(TEXT, nullable=True)
