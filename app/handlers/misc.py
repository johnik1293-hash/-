from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def on_help(m: types.Message):
    await m.answer(
        "Команды:\n"
        "/solve — решает уравнение (пример: x^2 - 5*x + 6 = 0)\n"
        "/quiz <тема> [n] — генерирует n вопросов\n"
        "/explain <тема> — краткий конспект\n"
        "\nСоветы: старайтесь формулировать темы конкретнее (например, 'фотосинтез', 'Куликовская битва')."
    )
