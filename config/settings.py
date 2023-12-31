from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Nanny app'
    DATABASE_URL: str

    BASE_DIR: Path = Path(__file__).resolve(strict=True).parent.parent
    APPS_DIR: Path = str(BASE_DIR) + "/apps"
    ORIGINS: list

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
