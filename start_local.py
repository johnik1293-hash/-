import asyncio
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from app.bot import dp
from app.handlers import start as h_start, solve as h_solve, quiz as h_quiz, explain as h_explain, misc as h_misc, tma as h_tma
from app.config import settings
from app.db import init_db

for r in (h_start.router, h_solve.router, h_quiz.router, h_explain.router, h_misc.router, h_tma.router):
    dp.include_router(r)

async def main():
    await init_db(settings.DB_PATH)
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    print("Bot polling started…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
