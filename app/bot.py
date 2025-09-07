from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.config import settings

# Проверим, что токен вообще задан в окружении Render
if not settings.BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is empty. Set it in Render → Environment variables.")

# Создаём бота с реальным токеном из ENV
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()
dp.include_router(router)
