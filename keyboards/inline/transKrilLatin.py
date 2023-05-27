from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

K_L_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='yes'),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)