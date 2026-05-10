from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧮 Решить задачу"), KeyboardButton(text="📝 Тест по теме")],
        [KeyboardButton(text="📚 Объяснить тему"), KeyboardButton(text="ℹ️ Помощь")],
        [KeyboardButton(text="🎮 О Mini Apps")],
    ],
    resize_keyboard=True
)
