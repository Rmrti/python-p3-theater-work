from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import object_session

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
    auditions = relationship("Audition", back_populates="role", lazy="dynamic")

    def actors(self):
        
        session = object_session(self)
        return [actor.name for actor in session.query(Actor).join(Audition).filter(Audition.role_id == self.id).all()]

    def locations(self):
        
        session = object_session(self)
        return [loc for (loc,) in session.query(Audition.location).filter(Audition.role_id == self.id).distinct().all()]

    def lead(self):
        
        session = object_session(self)
        lead_audition = session.query(Audition).filter(Audition.role_id == self.id, Audition.hired == True).order_by(Audition.id).first()
        return lead_audition if lead_audition else "no actor has been hired for this role"

    def understudy(self):
        
        session = object_session(self)
        hired_auditions = session.query(Audition).filter(Audition.role_id == self.id, Audition.hired == True).order_by(Audition.id).all()
        return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for understudy for this role"



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
    
    
