from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean
from sqlalchemy.orm import relationship, backref,joinedload
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

    def hired_auditions(self):
        session = object_session(self)
        return (
            session.query(Audition)
            .options(joinedload(Audition.actor))  
            .filter_by(role_id=self.id, hired=True)
            .order_by(Audition.id.asc())
            .all()
        )

    def lead(self):
        hired = self.hired_auditions()
        if hired:
            return hired[0].actor.name
        return "No actor has been hired for this role."

    def understudy(self):
        hired = self.hired_auditions()
        if len(hired) > 1:
            return  hired[1].actor.name
        return "No actor has been hired as an understudy for this role."


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
    
    
