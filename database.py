from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///email_history.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)