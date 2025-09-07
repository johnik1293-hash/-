from aiogram import Router, types
from aiogram.filters import Command
from app.services.quizgen import make_quiz
from app.db import get_db
from app.services.limiter import check_and_inc
from app.config import settings

router = Router()

@router.message(Command("quiz"))
async def on_quiz(m: types.Message):
    parts = m.text.split(maxsplit=2)
    if len(parts) < 2:
        await m.answer("Формат: /quiz <тема> [кол-во вопросов]\nНапр.: /quiz клетка 5")
        return
    topic = parts[1]
    n = int(parts[2]) if len(parts) == 3 and parts[2].isdigit() else 5

    db = await get_db(settings.DB_PATH)
    ok = await check_and_inc(db, m.from_user.id)
    await db.close()
    if not ok:
        await m.answer("Лимит на сегодня исчерпан. Нажмите кнопку PRO, чтобы снять ограничения.")
        return

    quiz = make_quiz(topic, n)
    if not quiz:
        await m.answer("Тема не найдена. Попробуйте другое слово.")
        return

    text = []
    for i, q in enumerate(quiz, 1):
        opts = "\n".join([f"{j}) {o}" for j, o in zip("ABCD", q['options'])])
        text.append(f"<b>{i}.</b> {q['q']}\n{opts}")
    await m.answer("\n\n".join(text))
    # Отправляем ключи для самопроверки
    keys = ", ".join(str(i)+":"+q['answer'] for i, q in enumerate(quiz, 1))
    await m.answer(f"Ответы: {keys}")
