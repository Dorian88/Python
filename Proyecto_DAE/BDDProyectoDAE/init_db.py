from config.database import engine, Base
import models

if __name__ == "__main__":
    #Crear todas las tablas en la BD apuntada por engine (DATABASE_URL)
    Base.metadata.create_all(bind = engine)
    print("Todas las tablas creadas correctamente en PostgreSQL")