from aiogram import Router, types
from aiogram.filters import CommandStart
from app.keyboards import main_kb

router = Router()

@router.message(CommandStart())
async def on_start(m: types.Message):
    await m.answer(
        "Привет! Я <b>Учебный помощник</b>.\n\n"
        "Я умею:\n"
        "• 🧮 решать базовые алгебраические задачи (уравнения)\n"
        "• 📝 делать тесты по теме\n"
        "• 📚 объяснять сложные темы кратко\n\n"
        "Команды: /solve, /quiz, /explain, /help",
        reply_markup=main_kb
    )
