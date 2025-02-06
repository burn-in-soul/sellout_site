from pydantic import Field, BaseModel


class DatabaseConfig(BaseModel):
    login: str = Field(..., title="Логин для подключения к базе данных")
    password: str = Field(..., title="Пароль для подключения к базе данных")
    host: str = Field(..., title="Хост для подключения к базе данных")
    port: int = Field(..., title="Порт для подключения к базе данных")
    name: str = Field(..., title="Имя базы данных")
    engine: str = Field(..., title="Бекенд базы данных")

    @property
    def dsn(self) -> str:
        return f"postgresql+asyncpg://{self.login}:{self.password}@{self.host}:{self.port}/{self.name}"

    @property
    def django_config(self) -> dict[str, str | int]:
        return {
            "ENGINE": self.engine,
            "NAME": self.name,
            "USER": self.login,
            "PASSWORD": self.password,
            "HOST": self.host,
            "PORT": self.port,
        }
