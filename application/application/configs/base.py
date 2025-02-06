from pathlib import Path
from pydantic import BaseModel, Field

from application.application.configs.database import DatabaseConfig
from application.application.configs.environment import EnvironmentConfig


class AppConfig(BaseModel):
    databases: DatabaseConfig = Field(..., title="Бд")
    environment: EnvironmentConfig = Field(..., title="Окружение")


def get_config():
    from os.path import join, dirname, realpath

    config_data = Path(join(dirname(realpath(__file__)), "../../../config.json")).read_text()
    return AppConfig.model_validate_json(config_data)


config = get_config()
