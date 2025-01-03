from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    log_path: str = "./logs/{time:YYYY-MM-DD!UTC}.log"
    parse_mode: str = "HTML"
    telegram_admin_username: str


settings = Settings()
