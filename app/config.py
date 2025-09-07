from pydantic import BaseModel
import os

class Settings(BaseModel):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    BASE_WEBHOOK_URL: str = os.getenv("BASE_WEBHOOK_URL", "")
    ADMIN_ID: int = int(os.getenv("ADMIN_ID", "0"))
    DB_PATH: str = os.getenv("DB_PATH", "./data/bot.db")

settings = Settings()
