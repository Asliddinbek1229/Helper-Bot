import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command

from keyboards.inline.subscription import chek_button
from keyboards.default.menuKeyboards import menuKeyboard
from utils.misc.subscription import chek
from data.config import CHANNELS

from filters import AdminFilter

from loader import dp, bot

users = []
users = set(users)
user_name = []
user_name = set(user_name)

@dp.message_handler(commands=['start'])
async def show_channels(message: types.Message):
    user = message.from_user.id
    users.add(user)
    mention = message.from_user.get_mention()
    user_n = message.from_user.full_name
    user_name.add(user_n)
    if user in users:
        await bot.send_message(chat_id=982935447, text=f"Guruhda yangi a'zo bor. {mention}")
    subscription = int()
    for channel in CHANNELS:
        status = await chek(user_id=message.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            subscription += 1

    if subscription == 2:
        await message.answer("Quyidagilardan birini tanlang👇👇👇", reply_markup=menuKeyboard)
    else:
        await message.answer(f"Quyidagi kanallarga obuna bo'ling: 👇",
                        reply_markup=chek_button,
                        disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    subscription = int()
    for channel in CHANNELS:
        status = await chek(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            subscription += 1

    if subscription == 2:
        await call.message.delete()
        await call.message.answer(
            "Siz botdan foydalanishingiz mumkin\nQuyidagilardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    else:
        await call.message.answer("Botdan foydalanish uchun barcha kanallarga obuna bo'ling!!!", disable_web_page_preview=True)


@dp.message_handler(commands=['statistika'])
async def statis(msg: types.Message):
    await msg.answer(f"Bot foydalanuvchilari soni {len(users)}")
    text = ""
    try:
        for user in user_name:
            text += f"\n. {user}"
        await msg.answer(text)
    except Exception as er:
        await msg.answer(er)
             