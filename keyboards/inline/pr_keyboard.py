from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

prayer_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👁 Ko'rish", callback_data='view'),
            InlineKeyboardButton(text="🔙 ortga", callback_data='back')
        ],
    ],
)