#!/bin/bash

# 가상환경 활성화 (venv 폴더가 있다고 가정)
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# DB 마이그레이션
python manage.py migrate

# static 파일 모으기
python manage.py collectstatic --noinput

# Gunicorn으로 서버 실행 (백그라운드)
gunicorn todo_project.wsgi:application --bind 0.0.0.0:8000 --daemon

echo "배포 완료! Gunicorn이 8000번 포트에서 실행 중입니다." 