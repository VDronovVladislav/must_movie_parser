from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declared_attr, declarative_base


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Movie(Base):
    name = Column(String(128), nullable=False)
    image = Column(String(255))
