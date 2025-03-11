from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# tb_id = Column(Integer, primary_Key= True, autoincrement=True)

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key= True, autoincrement=True)

    name = Column(String, nullable=False)
    auditions = relationship("Audition", back_populates="actor")
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key= True, autoincrement=True)
    character_name=Column(String, nullable=False)
    auditions = relationship("Audition", back_populates="role")

    #method to return all actors in for this role
    
    def actors(self):
        for audition in self.auditions:
            return [audition.actor.name]
        

class Audition(Base):
    __tablename__ = "auditions"
    id = Column(Integer, primary_key= True, autoincrement=True)
    actor_id = Column(Integer, ForeignKey("actors.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    location= Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired= Column(Boolean, nullable=False)

    #Relationships
    actor = relationship("Actor", back_populates="auditions")
    role = relationship("Role", back_populates="auditions")

    def call_back(self):
        self.hired = True
    
    
