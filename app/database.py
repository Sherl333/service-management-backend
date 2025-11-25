from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.exc import OperationalError
import time
from .config import settings

#This raw connection (conn & cur) isn’t used in the ORM part of the app. It’s mostly a “ping check” to ensure DB connectivity.
"""while True:
  try:
      # Connect to the PostgreSQL server
      conn = psycopg2.connect(
          host="localhost",
          dbname="fastapi",
          user="postgres",
          password="Praise@97",
          port=5432,  # Default PostgreSQL port
          cursor_factory = RealDictCursor

      )

      # Create a cursor object
      cur = conn.cursor()   
      print("database connected!")
      break
  except Exception as e:
      print(f"Error connecting to PostgreSQL: {e}")  
      time.sleep(2)  """


# This is a dependency you’ll use in your FastAPI routes.
# It creates a new DB session, gives it to the request handler, and then closes it once the request is done.
def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

#Connection string for SQLAlchemy ORM.... Uses the psycopg2 driver under the hood.
DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Create engine
#the core DB connection object for SQLAlchemy.
while True:
    try:
        engine = create_engine(DATABASE_URL)
        print("✅ Database connected!")
        break
    except OperationalError as e:
        print(f"❌ DB Connection failed: {e}")
        time.sleep(2)

# Session maker
# Sessions are how you interact with the DB in SQLAlchemy ORM.
# autocommit=False → you need to explicitly commit changes.
# autoflush=False → prevents accidental flushing of uncommitted data.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
# All your ORM models (Posts, Users, etc.) inherit from Base.
# This lets SQLAlchemy know which classes map to database tables.
Base = declarative_base()