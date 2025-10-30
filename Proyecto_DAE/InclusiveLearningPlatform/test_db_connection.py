import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        connection = psycopg2.connect(
            dbname="inclusive_learning",
            user="udea_user",
            password="udea123",
            host="localhost",
            port="5432"
        )
        print("✅ Conexión exitosa a PostgreSQL")
        connection.close()
    except OperationalError as e:
        print("❌ Error al conectar a PostgreSQL:")
        print(e)

if __name__ == "__main__":
    test_connection()