from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🧮 Решить задачу"), KeyboardButton(text="📝 Тест по теме")],
        [KeyboardButton(text="📚 Объяснить тему"), KeyboardButton(text="ℹ️ Помощь")],
        [KeyboardButton(text="🎮 О Mini Apps")],
    ],
    resize_keyboard=True
)

def get_game_kb(url: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🎮 Запустить прототип HoMM3", web_app=WebAppInfo(url=f"{url}/static/index.html"))]
        ]
    )
