import os
from db import get_connection

def init_database():
    # 프로젝트 루트를 찾아서 schema.sql 경로로 만들기
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    schema_path = os.path.join(BASE_DIR,"sql" ,"schema.sql")

    print("Using schema file:", schema_path)

    conn = get_connection()
    cur = conn.cursor()

    with open(schema_path, "r") as f:
        sql = f.read()

    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()