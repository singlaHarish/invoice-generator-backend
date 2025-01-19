from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:abcde12345@192.168.0.176:3306/invoicegen"
#DATABASE_URL = "mysql+mysqlconnector://root:abcde12345@localhost:3306/invoicegen"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
