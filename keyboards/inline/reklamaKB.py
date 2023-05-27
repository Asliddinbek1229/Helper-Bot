from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

rek_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Matn", callback_data='text'),
        ],
    ],
)