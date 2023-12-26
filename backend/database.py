```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
DATABASE_URI = 'postgresql://user:password@localhost:5432/codebuddy'

# Create SQLAlchemy engine and session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Base class for models
Base = declarative_base()

class UserQuery(Base):
    __tablename__ = 'user_queries'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    query = Column(String(500))
    timestamp = Column(DateTime)

class UserPreference(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    preference = Column(String(50))

class UserHistory(Base):
    __tablename__ = 'user_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50))
    action = Column(String(500))
    timestamp = Column(DateTime)

# Create tables
Base.metadata.create_all(engine)

def add_record(record):
    session = Session()
    session.add(record)
    session.commit()

def get_records_by_user_id(table, user_id):
    session = Session()
    records = session.query(table).filter_by(user_id=user_id).all()
    return records
```
