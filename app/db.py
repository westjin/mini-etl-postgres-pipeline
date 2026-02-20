import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        dbname="etl_db",
        user="seojin",
        password="1234"
    )
    return conn