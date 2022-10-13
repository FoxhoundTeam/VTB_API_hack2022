from typing import Any, Dict, Optional

from pydantic import BaseSettings, MongoDsn, validator


class Settings(BaseSettings):
    project_name: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expires_s: int = 60 * 60 * 60

    mongodb_server: str
    mongodb_db: str = "api"
    database_uri: Optional[MongoDsn] = None

    @validator("database_uri", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return MongoDsn.build(
            scheme="mongodb",
            host=values.get("mongodb_server"),
            path=f"/{values.get('mongodb_db') or ''}",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
