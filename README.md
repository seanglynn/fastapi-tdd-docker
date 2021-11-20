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
# Run individual containers
docker build -t tdd-fastapi project
docker run -p 8000:8000 tdd-fastapi

# docker-compose build/deploy
docker-compose build
docker-compose up
# docker-compose access postgres sql
docker-compose exec web-db psql -U postgres
# docker-compose logs
docker-compose logs web
docker-compose logs web-db

# docker-compose init db
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
# docker-compose migrate db (1)
docker-compose exec web aerich init-db

# psql shell cmds (web_dev db)
postgres=# \c web_dev
web_dev=# \dt

```
