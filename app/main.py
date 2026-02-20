from db import get_connection

def test_connection():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    result = cur.fetchone()
    print("PostgreSQL version:")
    print(result)
    cur.close()
    conn.close()

if __name__ == "__main__":
    test_connection()
