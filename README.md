# FastAPI TDD Docker
Lab files from: https://testdriven.io/courses/tdd-fastapi/

## Get Started
#### Poetry Commands
```
poetry install -v
poetry update
poetry run uvicorn app.main:app --reload
poetry export --without-hashes -o requirements.txt
```

#### Docker Commands
```
docker build -t tdd-fastapi project
docker run -p 8000:8000 tdd-fastapi

docker-compose build
docker-compose up
```
