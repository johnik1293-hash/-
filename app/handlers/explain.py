from aiogram import Router, types
from aiogram.filters import Command
from app.services.explainer import explain
from app.db import get_db
from app.services.limiter import check_and_inc
from app.config import settings

router = Router()

@router.message(Command("explain"))
async def on_explain(m: types.Message):
    parts = m.text.split(maxsplit=1)
    if len(parts) < 2:
         await m.answer("Формат: /explain <тема>", parse_mode=None)
        return
    topic = parts[1]

    db = await get_db(settings.DB_PATH)
    ok = await check_and_inc(db, m.from_user.id)
    await db.close()
    if not ok:
        await m.answer("Лимит на сегодня исчерпан. Нажмите кнопку PRO, чтобы снять ограничения.")
        return

    res = explain(topic)
    if not res:
        await m.answer("Тема не найдена. Попробуйте другое слово.")
        return
    summary, bullets = res
    await m.answer(f"<b>Кратко:</b> {summary}")
    if bullets:
        await m.answer("\n".join("• " + b for b in bullets))
