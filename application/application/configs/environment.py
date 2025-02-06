from pydantic import Field, BaseModel


class EnvironmentConfig(BaseModel):
    debug: bool = Field(False, title="Дебаг")
    secret_key: str = Field(..., title="Секрет")
    allowed_hosts: list[str] = Field(..., title="Хосты")
