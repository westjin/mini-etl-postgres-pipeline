import csv
from db import get_connection

def is_valid_email(email):
    """
    아주 간단한 이메일 포맷 확인 함수
    '@' 포함 여부만 체크
    (필요하면 정규표현식으로 확장 가능)
    """
    return "@" in email and "." in email

def run_etl():
    conn = get_connection()
    cur = conn.cursor()

    inserted_count = 0
    skipped_count = 0

    with open("data/sample_users.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["name"]
            email = row["email"]

            # --- 검증 (Transform) ---
            if not is_valid_email(email):
                print(f"[SKIP] Invalid email: {email}")
                skipped_count += 1
                continue

            # --- 적재 (Load) ---
            try:
                cur.execute(
                    "INSERT INTO users (name, email) VALUES (%s, %s)",
                    (name, email)
                )
                inserted_count += 1
            except Exception as e:
                print(f"[ERROR] Insert failed for {name}, {email} -> {e}")
                conn.rollback()
                continue

    # 최종 커밋
    conn.commit()

    # 리소스 정리
    cur.close()
    conn.close()

    print("------- ETL SUMMARY -------")
    print(f"Inserted rows : {inserted_count}")
    print(f"Skipped rows  : {skipped_count}")
    print("---------------------------")

if __name__ == "__main__":
    run_etl()