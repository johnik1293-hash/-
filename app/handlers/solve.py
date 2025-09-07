from aiogram import Router, types, F
from aiogram.filters import Command
from sympy import Eq, symbols, solve, sympify
from app.db import get_db
from app.services.limiter import check_and_inc
from app.config import settings

router = Router()

@router.message(Command("solve"))
async def on_solve_help(m: types.Message):
    await m.answer("Пришлите уравнение, например: x^2 - 5*x + 6 = 0")

@router.message(F.text.regexp(r"=.*"))
async def handle_equation(m: types.Message):
    # Лимит
    db = await get_db(settings.DB_PATH)
    ok = await check_and_inc(db, m.from_user.id)
    await db.close()
    if not ok:
        await m.answer("Лимит на сегодня исчерпан. Нажмите кнопку PRO, чтобы снять ограничения.")
        return

    try:
        left, right = m.text.split('=')
        x = symbols('x')
        eq = Eq(sympify(left.replace('^', '**')), sympify(right.replace('^', '**')))
        roots = solve(eq, x)
        await m.answer(f"Решение: <code>{roots}</code>")
    except Exception as e:
        await m.answer("Не удалось разобрать уравнение. Пример: x^2 - 5*x + 6 = 0")
