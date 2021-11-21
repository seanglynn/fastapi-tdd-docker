import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

# See LRU Cache: https://docs.python.org/3/library/functools.html#functools.lru_cache
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
