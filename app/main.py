# app/main.py
from fastapi import FastAPI, Request
from aiogram.types import Update
from app.bot import dp, bot
from app.handlers import start as h_start, solve as h_solve, quiz as h_quiz, explain as h_explain, misc as h_misc, pro as h_pro
from app.config import settings
from app.db import init_db
from fastapi.responses import PlainTextResponse

for r in (h_start.router, h_solve.router, h_quiz.router, h_explain.router, h_misc.router, h_pro.router):
    dp.include_router(r)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db(settings.DB_PATH)
    if settings.BASE_WEBHOOK_URL:
        wh_url = f"{settings.BASE_WEBHOOK_URL}/webhook/{settings.BOT_TOKEN}"
        try:
            await bot.set_webhook(url=wh_url, drop_pending_updates=True)
        except Exception as e:
            print("Webhook set error:", e)

@app.on_event("shutdown")
async def on_shutdown():
    try:
        await bot.session.close()
    except Exception:
        pass

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    if token != settings.BOT_TOKEN:
        return {"status": "forbidden"}
    data = await request.json()
    try:
        update = Update.model_validate(data)
        await dp.feed_update(bot, update)
    except Exception as e:
        # важный лог: видно, какой апдейт ломается
        print("Update processing error:", repr(e), "| update:", data)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "ok"}

@app.head("/")
async def root_head():
    return PlainTextResponse("ok")
