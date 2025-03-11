from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Actor, Role, Audition

# Create an SQLite engine (Ensure this matches your database)
engine = create_engine("sqlite:///db.sqlite3")  # Use a separate test DB to avoid conflicts


# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Create tables (only for testing)
Base.metadata.drop_all(engine)  # Clears previous test data
Base.metadata.create_all(engine)  # Recreates tables

# Insert test data
actor1 = Actor(name="Leonardo DiCaprio")
actor2 = Actor(name="Tom Hanks")
actor3 = Actor(name="Meryl Streep")

role1 = Role(character_name="Jack Dawson")
role2 = Role(character_name="Forrest Gump")

audition1 = Audition(actor=actor1, role=role1, location="Los Angeles", phone=123456789, hired=True)
audition2 = Audition(actor=actor2, role=role1, location="New York", phone=987654321, hired=False)
audition3 = Audition(actor=actor3, role=role2, location="Chicago", phone=555555555, hired=True)
audition4 = Audition(actor=actor1, role=role2, location="Atlanta", phone=123123123, hired=True)  # Second hire

# Add to session and commit
session.add_all([actor1, actor2, actor3, role1, role2, audition1, audition2, audition3, audition4])
session.commit()

# Fetch roles to test methods
role = session.query(Role).filter_by(character_name="Jack Dawson").first()
role2 = session.query(Role).filter_by(character_name="Forrest Gump").first()

print("\n=== Testing Role Methods ===")
print("Actors who auditioned for Jack Dawson:", role.actors())  
print("Audition locations for Jack Dawson:", role.locations())  

print("Lead actor for Jack Dawson:", role.lead())  
print("Understudy for Jack Dawson:", role.understudy())  

print("Lead actor for Forrest Gump:", role2.lead())  
print("Understudy for Forrest Gump:", role2.understudy())  

print("\n=== Testing Audition Callback ===")
print("Before call_back(), Hired Status of Tom Hanks:", audition2.hired)  
audition2.call_back()  # Change status to hired
session.commit()

print("After call_back(), Hired Status of Tom Hanks:", audition2.hired)  
print("New Lead actor for Jack Dawson:", role.lead())  
