from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuKeyboard = ReplyKeyboardMarkup(
    one_time_keyboard=True,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🕋 Namoz vaqtlarini ko'rish"),
        ],
        [
            KeyboardButton(text="🔁 Tarjimon"),
            KeyboardButton(text="🌐 Wikipedia"),
        ],
        [
            KeyboardButton(text="🗣 Speak English"),
            KeyboardButton(text="✅ So'zlarni tekshirish"),
        ],
        [
            KeyboardButton(text="♻️ Krill-lotin"),
        ],
    ],
)