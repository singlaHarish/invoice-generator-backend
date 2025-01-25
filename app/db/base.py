from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.logConfig import logger

#DATABASE_URL = "mysql+mysqlconnector://root:12345@localhost:3306/invoicegen"

# Create an in-memory SQLite database
DATABASE_URL = "sqlite:///:memory:"

#engine = create_engine(DATABASE_URL)
# Create engine with multi-threading support
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Allow multi-threaded access
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
db = SessionLocal()
def get_db():
    #db = SessionLocal()
    logger.info(f"Session id: {id(db)}")
    try:
        yield db
    finally:
        #db.close()
        pass

# def create_connection():
#     try:
#         connection = mysql.connector.connect(
#             host="",
#             user="",
#             password="",
#             database=""
#         )
#         return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None
