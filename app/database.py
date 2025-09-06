from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session

# 1. The Engine (Power Plant) 
# This URL tells your app how to find and connect to the database.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


# 2. The Session (Workshop) 
# This creates a "factory" for making new database sessions (workshops).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 3. The Base (Blueprint Central) - THIS IS THE KEY CHANGE
# All your models will inherit from this Base class.
# In older versions, it was imported from sqlalchemy.ext.declarative.
# Now, it's directly in sqlalchemy.orm.
Base = declarative_base()

def get_db():
    # 1. Get a new, clean session (a personal cooking station)
    db = SessionLocal()
    try:
        # 2. Provide this session to the API request
        yield db
    finally:
        # 3. After the request is done, close the session
        db.close()