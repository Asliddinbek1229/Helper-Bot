from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

trans_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿UZ - 🏴󠁧󠁢󠁥󠁮󠁧󠁿EN", callback_data='uz_en'),
            InlineKeyboardButton(text='🏴󠁧󠁢󠁥󠁮󠁧󠁿EN - 🇺🇿UZ', callback_data='en_uz'),
        ],
        [
            InlineKeyboardButton(text='🔙 ortga', callback_data='orqaga')
        ]
    ],
)

back_to = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='yes'),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)