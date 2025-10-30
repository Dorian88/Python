from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambiar usuario, password, host, y nombre de BD según tu entorno
DATABASE_URL = "postgresql://postgres:admin@localhost/inclusive_learning_db" # Reemplar tu_password y inclusive_learning_db por los que uso

engine = create_engine(DATABASE_URL, echo = True) #echo = true para ver SQL en consola
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)
Base = declarative_base()