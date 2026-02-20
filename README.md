📌 Mini ETL PostgreSQL 파이프라인

📖 프로젝트 소개

이 프로젝트는 Python과 PostgreSQL을 이용하여 **ETL(Extract → Transform → Load)**의 기본 흐름을 구현한 토이 프로젝트입니다.
CSV 파일 데이터를 읽어와 정제한 후, PostgreSQL에 적재하는 전체 과정을 경험할 수 있습니다.

⸻

📂 폴더 구조

다음과 같은 구조로 구성되어 있습니다.
	•	app/
	•	db.py : PostgreSQL 연결 코드
	•	init_db.py : DB 테이블 자동 생성 스크립트
	•	etl.py : CSV → DB ETL 처리 코드
	•	data/
	•	sample_users.csv : 예시 데이터
	•	sql/
	•	schema.sql : 테이블 정의 SQL
	•	docker-compose.yml : Docker PostgreSQL 구성
	•	requirements.txt : Python 의존성
	•	README.md : 이 문서

⸻

🚀 설치 & 실행 방법
	1.	저장소 클론
git clone https://github.com/<your-id>/mini-etl-postgres-pipeline.git
cd mini-etl-postgres-pipeline
	2.	Docker PostgreSQL 실행
docker compose up -d
	3.	Python 가상환경 설정
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
	4.	DB 테이블 자동 생성
python app/init_db.py
	5.	ETL 실행
python app/etl.py

⸻

🧠 ETL 흐름 설명

1. 추출 (Extract)

CSV 파일에서 데이터를 한 줄씩 읽어옵니다.
이 단계에서 원본(raw) 데이터를 확보합니다.

샘플 파일: data/sample_users.csv

⸻

2. 정제 (Transform)

읽어온 데이터를 검증합니다.
예를 들어 이메일 형식이 올바르지 않은 데이터는 스킵합니다.

⸻

3. 적재 (Load)

정제된 데이터를 PostgreSQL 데이터베이스의 users 테이블에 INSERT합니다.
정상 데이터와 스킵된 데이터 수를 요약하여 출력합니다.

⸻

📊 실행 결과 예시

정제가 필요한 데이터가 포함된 CSV를 처리하면 다음과 같은 결과가 나옵니다:
'''
[SKIP] Invalid email: bob_at_example.com  
[SKIP] Invalid email: davidexample.com  
Inserted rows : 3  
Skipped rows : 2
'''


⸻

📌 배운 점
	•	ETL의 기본 구조(Extract → Transform → Load)를 직접 구현해봤습니다.
	•	Docker 기반 PostgreSQL 환경을 구성했습니다.
	•	Python으로 DB 연결 및 SQL 실행을 자동화했습니다.
	•	데이터 정제 및 예외 처리 로직을 적용했습니다.

⸻

🤝 참고

ETL은 데이터 파이프라인의 기본 개념으로, 실제 업무에서는 파일, API, 데이터브릭 등 다양한 데이터 소스와 함께 사용됩니다.
이 프로젝트는 그 기본 흐름을 이해하기 위한 예제입니다.
