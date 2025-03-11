# 🎭 SQLAlchemy Theater Audition Management

## 📌 Project Overview
This project is a simple **Theater Audition Management System** built using **SQLAlchemy**. It allows you to manage actors, roles, and auditions, including hiring lead actors and understudies for specific roles.

## 🏗 Features
- Manage **Actors**, **Roles**, and **Auditions**.
- Retrieve actors who auditioned for a specific role.
- Get a list of unique audition **locations** for a role.
- Identify the **lead actor** and **understudy** for a role.
- Mark an audition as **hired** using a callback method.
- Uses **SQLAlchemy ORM** for database interactions.

## 🛠 Technologies Used
- Python 3
- SQLAlchemy (ORM)
- SQLite (Default Database)

---

## 📂 Project Structure
```
📦 your_project_folder
 ┣ 📂 lib
 ┃ ┣ 📜 models.py  # Contains SQLAlchemy models and methods
 ┃ ┣ 📜 database.py  # Manages database connections
 ┣ 📜 test_models.py  # Contains test cases for models
 ┣ 📜 README.md  # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your_username/theater-audition-management.git
cd theater-audition-management
```

### 2️⃣ Install Dependencies
Create a virtual environment and install required packages:
```sh
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt  # If you have a requirements file
```
OR manually install SQLAlchemy:
```sh
pip install sqlalchemy
```

### 3️⃣ Setting Up the Database
Run the following command in Python to create the database tables:
```python
from lib.models import Base
from sqlalchemy import create_engine

db_url = "sqlite:///auditions.db"  # Change this to your preferred database
engine = create_engine(db_url)
Base.metadata.create_all(engine)
print("Database initialized successfully!")
```

### 4️⃣ Running Tests
To test the methods, run:
```sh
python test_models.py
```
This will output details about auditions, hired actors, and more.

---

## 📖 Model Descriptions

### 🎭 Actor Model
| Field  | Type    | Description        |
|--------|--------|--------------------|
| `id`   | Integer | Primary Key       |
| `name` | String  | Actor's Name      |
| `auditions` | Relationship | Linked Auditions |

### 🎬 Role Model
| Field  | Type    | Description        |
|--------|--------|--------------------|
| `id`   | Integer | Primary Key       |
| `character_name` | String | Role Name |
| `auditions` | Relationship | Linked Auditions |

#### Role Methods
- `actors()`: Returns actors who auditioned for this role.
- `locations()`: Returns unique locations where the auditions took place.
- `lead()`: Returns the lead actor for this role.
- `understudy()`: Returns the understudy actor (if available).

### 🎤 Audition Model
| Field  | Type    | Description        |
|--------|--------|--------------------|
| `id`   | Integer | Primary Key       |
| `actor_id` | Integer | Foreign Key (Actor) |
| `role_id` | Integer | Foreign Key (Role) |
| `location` | String | Audition Location |
| `phone` | Integer | Actor's Phone Number |
| `hired` | Boolean | Hiring Status |

#### Audition Methods
- `call_back()`: Marks the actor as hired.

---

## 🏆 Example Usage
```python
from lib.models import Actor, Role, Audition
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///auditions.db")
Session = sessionmaker(bind=engine)
session = Session()

# Add new actor
actor1 = Actor(name="Leonardo DiCaprio")
session.add(actor1)
session.commit()

# Add new role
role1 = Role(character_name="Jack Dawson")
session.add(role1)
session.commit()

# Add an audition
audition1 = Audition(actor_id=actor1.id, role_id=role1.id, location="Los Angeles", phone=1234567890, hired=False)
session.add(audition1)
session.commit()

# Get lead actor
print(role1.lead())
```

---

## 🛠 Troubleshooting
1. **ModuleNotFoundError: No module named 'sqlalchemy'**
   - Ensure SQLAlchemy is installed: `pip install sqlalchemy`
2. **Database table does not exist**
   - Run `Base.metadata.create_all(engine)` to create tables.
3. **Objects returning as memory addresses (`<lib.models.Audition object at 0x7e9...>` instead of names)**
   - Ensure you are accessing attributes correctly (e.g., `audition.actor.name`).

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

📌 **Happy Coding! 🎭🎬**

