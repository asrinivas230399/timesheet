from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL database connection URL
DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"

# Create a database engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,  # Maximum number of connections in the pool
    max_overflow=20,  # Maximum number of connections to open beyond the pool_size
    pool_timeout=30,  # Maximum number of seconds to wait for a connection from the pool
    pool_recycle=1800  # Number of seconds after which a connection is automatically recycled
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create the database tables
Base.metadata.create_all(bind=engine)
