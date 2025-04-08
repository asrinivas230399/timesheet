import databases
import sqlalchemy
from sqlalchemy.pool import QueuePool

DATABASE_URL = "mysql://user:password@localhost/dbname"

# Create a database connection with connection pooling
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    poolclass=QueuePool,  # Use QueuePool for connection pooling
    pool_size=5,          # The size of the pool to maintain
    max_overflow=10,      # The maximum overflow size
    pool_timeout=30,      # The maximum time to wait for a connection
    pool_recycle=1800     # The time to recycle connections
)

database = databases.Database(DATABASE_URL)

async def connect_db():
    await database.connect()

async def disconnect_db():
    await database.disconnect()
