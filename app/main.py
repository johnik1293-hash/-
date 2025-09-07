import os
from fastapi import FastAPI, Request
from aiogram import Bot
from aiogram.types import Update
from app.bot import dp, bot
from app.handlers import start as h_start, solve as h_solve, quiz as h_quiz, explain as h_explain, misc as h_misc
from app.config import settings
from app.db import init_db

# Подключаем роутеры
for r in (h_start.router, h_solve.router, h_quiz.router, h_explain.router, h_misc.router):
    dp.include_router(r)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    # Патч токена в bot (установим из env)
    bot._token = settings.BOT_TOKEN
    await init_db(settings.DB_PATH)
    # Устанавливаем вебхук
    if settings.BASE_WEBHOOK_URL:
        wh_url = f"{settings.BASE_WEBHOOK_URL}/webhook/{settings.BOT_TOKEN}"
        try:
            await Bot(settings.BOT_TOKEN).set_webhook(url=wh_url, drop_pending_updates=True)
        except Exception as e:
            print("Webhook set error:", e)

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    if token != settings.BOT_TOKEN:
        return {"status": "forbidden"}
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "ok"}
