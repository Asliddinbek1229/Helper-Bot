from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



wiki_to = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha", callback_data='yes'),
            InlineKeyboardButton(text='🔙 ortga', callback_data='ortga'),
        ],
    ],
)