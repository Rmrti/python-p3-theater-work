from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_Key= True, autoincrement=True)

    name = Column(String, nullable=False)
    auditions = relationship("Audition", back_populates="actor")
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    character_name=Column(String, nullable=False)
    auditions = relationship("Audition", back_populates="actor")



