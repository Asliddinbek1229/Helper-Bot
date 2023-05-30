from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

rek_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Matn", callback_data='text'),
            InlineKeyboardButton(text="📸 Rasm", callback_data='r_photo'),
        ],
    ],
)