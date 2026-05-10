from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()

TMA_INFO = (
    "<b>Можно ли сделать игру типа HoMM3 в Telegram Mini App бесплатно?</b>\n\n"
    "Да, это вполне реально! Вот основные шаги и инструменты:\n\n"
    "1. 🌐 <b>Бесплатный хостинг:</b>\n"
    "• <b>GitHub Pages:</b> идеально для статических игр (HTML/JS/Assets).\n"
    "• <b>Vercel / Netlify:</b> отличные варианты с поддержкой Serverless функций, если нужен простой бэкенд.\n"
    "• <b>Render:</b> можно использовать для полноценного бэкенда (как в этом боте).\n\n"
    "2. 🎮 <b>Движки (Engine):</b>\n"
    "• <b>Phaser.js:</b> самый популярный 2D движок для браузерных игр. Огромное комьюнити.\n"
    "• <b>PixiJS:</b> если нужен только быстрый рендеринг 2D графики.\n"
    "• <b>Godot:</b> можно экспортировать игру в HTML5. Отличный визуальный редактор.\n"
    "• <b>HeroWO:</b> открытый движок на JS, специально созданный как клон HoMM3.\n\n"
    "3. 🎨 <b>Ресурсы (Assets):</b>\n"
    "• <b>OpenGameArt.org:</b> бесплатная графика и звуки.\n"
    "• <b>Itch.io (Free section):</b> качественные спрайты и тайлсеты.\n"
    "• <b>Kenney.nl:</b> качественные бесплатные ассеты в едином стиле.\n\n"
    "4. 🛠 <b>Интеграция с Telegram:</b>\n"
    "• Используйте <code>@telegram-apps/sdk</code> для связи игры с Telegram (данные пользователя, тема оформления).\n"
    "• Бот выступает «точкой входа», запуская Mini App через <code>WebAppInfo</code>.\n\n"
    "Используйте команду /tma, чтобы увидеть это сообщение снова!"
)

@router.message(Command("tma"))
@router.message(F.text == "🎮 О Mini Apps")
async def on_tma_info(m: types.Message):
    await m.answer(TMA_INFO)
