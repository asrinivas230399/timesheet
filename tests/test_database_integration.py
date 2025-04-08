import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, DATABASE_URL

# Create a new database engine for testing
TEST_DATABASE_URL = "sqlite:///./test_integration.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db_session():
    """Create a new database session for testing."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


def test_database_connection(db_session):
    """Test if the database connection is successful."""
    result = db_session.execute("SELECT 1").scalar()
    assert result == 1


def test_query_execution(db_session):
    """Test if a simple query can be executed."""
    # Assuming there is a Customer table
    result = db_session.execute("SELECT COUNT(*) FROM customers").scalar()
    assert result is not None