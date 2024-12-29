from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    telegram_devforce_group_id: str


settings = Settings()
