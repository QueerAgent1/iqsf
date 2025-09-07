from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password @localhost/iqsf")

engine = create_engine(DB_URL)
metadata = MetaData()
SessionLocal = sessionmaker(bind=engine)
