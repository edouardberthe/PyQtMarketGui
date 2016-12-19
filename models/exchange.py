from sqlalchemy import Column, String

from models.declarative_base import Base


class Exchange(Base):

    __tablename__ = 'exchange'

    ticker = Column(String(2), primary_key=True)
    name = Column(String(20))
