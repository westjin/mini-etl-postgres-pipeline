📌 Mini ETL PostgreSQL 파이프라인

📖 프로젝트 소개

이 리포지토리는 Python과 PostgreSQL을 이용해
ETL(추출 → 정제 → 적재) 파이프라인의 기본 흐름을 구현한 토이 프로젝트입니다.


⸻

📌 이 프로젝트는 다음과 같은 동작을 수행합니다:
	•	Docker로 PostgreSQL DB를 실행
	•	SQL 파일로 테이블 구조 자동 생성
	•	CSV 파일에서 데이터를 읽어서 정제 및 적재
	•	정제 기준을 통과하지 못한 데이터는 스킵
	•	최종적으로 적재 결과 요약 출력

⸻

📌 폴더 구조

프로젝트의 주요 구성은 아래와 같습니다:

📂 mini-etl-postgres-pipeline
├ app/
│  db.py ← DB 연결 코드
│  init_db.py ← 테이블 자동 생성 코드
│  etl.py ← ETL 파이프라인 코드
├ data/
│  sample_users.csv ← 예시 데이터
├ sql/
│  schema.sql ← Users 테이블 정의
├ docker-compose.yml
├ requirements.txt
└ README.md

⸻

📌 설치 & 실행
	1.	리포지토리 클론
git clone https://github.com//mini-etl-postgres-pipeline.git
cd mini-etl-postgres-pipeline
	2.	Docker PostgreSQL 실행
docker compose up -d
	3.	Python 의존성 설치
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
	4.	테이블 생성
python app/init_db.py
	5.	ETL 실행
python app/etl.py

⸻

📌 ETL 흐름 설명

1) 추출 (Extract)

CSV 파일에서 데이터를 한 줄씩 읽어옵니다.
이 단계에서 raw 데이터를 확보합니다.

예) sample_users.csv

⸻

2) 정제 (Transform)

읽어온 데이터를 검사합니다.
예) 이메일 형식이 맞는지 확인한 후, 맞지 않으면 스킵

⸻

3) 적재 (Load)

정제된 데이터를 PostgreSQL DB에 INSERT 합니다.
정상 적재된 수와 스킵된 수를 요약해서 출력합니다.

⸻

📝 실행 예시

정제가 필요한 데이터가 있을 때
아래와 같은 결과가 출력됩니다:

[SKIP] Invalid email: bob_at_example.com
[SKIP] Invalid email: davidexample.com
Inserted rows : 3
Skipped rows : 2

⸻

🎯 배운 점
	•	ETL의 기본 구조를 코드로 구현함
	•	Docker + PostgreSQL 환경 구성
	•	Python으로 DB 연결하고 데이터 적재
	•	데이터 정제 및 결과 요약 처리
