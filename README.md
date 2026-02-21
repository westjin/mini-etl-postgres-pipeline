# 📌 Mini ETL PostgreSQL 파이프라인

## 📖 프로젝트 소개

이 프로젝트는 Python과 PostgreSQL을 이용해 ETL(Extract → Transform → Load)의 기본 흐름을 구현한 토이 프로젝트입니다.  
CSV 데이터를 읽어서 정제하고, PostgreSQL에 저장하는 전체 과정입니다.

---

## 📂 폴더 구조

프로젝트는 아래와 같은 구조로 구성되어 있습니다:

```
mini-etl-postgres-pipeline/
├─ app/
│   ├ db.py              # PostgreSQL 연결 코드
│   ├ init_db.py         # DB 테이블 자동 생성 스크립트
│   └ etl.py             # ETL 처리 스크립트
├─ data/
│   └ sample_users.csv   # 예시 CSV 데이터
├─ sql/
│   └ schema.sql         # 테이블 정의 SQL
├─ docker-compose.yml    # Docker PostgreSQL 설정
├─ requirements.txt      # Python 라이브러리 목록
└─ README.md
```

---

## 🚀 설치 및 실행 방법

### 1) 저장소 클론

```bash
git clone https://github.com/<your-id>/mini-etl-postgres-pipeline.git
cd mini-etl-postgres-pipeline
```

---

### 2) Docker PostgreSQL 실행

```bash
docker compose up -d
```

---

### 3) Python 가상환경 설정

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 4) DB 테이블 생성

```bash
python app/init_db.py
```

---

### 5) ETL 실행

```bash
python app/etl.py
```

---

## 🧠 ETL 흐름 설명

### 🔹 1. 추출(Extract)

CSV 파일에서 데이터를 한 줄씩 읽어 옵니다.  
이 단계는 원본 데이터를 확보하는 과정입니다.

**샘플 파일:** `data/sample_users.csv`

---

### 🔹 2. 정제(Transform)

읽어온 데이터를 검증합니다.  
예: 이메일 형식이 올바르지 않은 경우 스킵 처리합니다.

---

### 🔹 3. 적재(Load)

정제된 데이터를 PostgreSQL DB의 `users` 테이블에 저장합니다.

---

## 💻 코드 예시

### Python DB 연결 테스트

```python
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
```

---

## ⚡ ETL 실행 예시

```bash
python app/etl.py
```

---

## 📊 실행 결과 예시

```
[SKIP] Invalid email: bob_at_example.com
[SKIP] Invalid email: davidexample.com
Inserted rows : 3
Skipped rows : 2
```

---

## 📌 배운 점

- ETL의 기본 구조(Extract → Transform → Load)를 직접 구현했습니다.  
- Docker 기반 PostgreSQL 환경 구성을 경험했습니다.  
- Python을 이용해 DB 연결 및 SQL 실행 자동화를 구현했습니다.  
- 데이터 정제 및 예외 처리 로직을 적용했습니다.

---

## 🤝 참고

이 프로젝트는 데이터 파이프라인의 기본 개념을 이해하기 위한 예제입니다.  


