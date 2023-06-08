import logging
import sqlite3

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.subscription import chek_button
from keyboards.default.menuKeyboards import menuKeyboard
from utils.misc.subscription import chek
from data.config import CHANNELS, ADMINS

from states.add_userState import AddState
from aiogram.dispatcher import FSMContext

from loader import dp, bot, db


@dp.message_handler(Command('start'))
async def show_channels(message: types.Message):
    user = message.from_user.id
    name = message.from_user.full_name
    try:
        db.add_user(id=user, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=982935447, text=err)

    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor"
    await bot.send_message(chat_id=982935447, text=msg)

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
    users = db.select_all_users()
    msg2 = f"Bot foydalanuvchilari soni {len(users)}"
    foydalanuvchi = ""
    num = 0
    for user in users:
        id = user[0]
        name = user[1]
        num += 1
        foydalanuvchi += f"\n{num}) {name}. {id}"
    await msg.answer(f"{msg2}\n"
                     f"{foydalanuvchi}")
        

@dp.message_handler(Command('add_user'))
async def add_user(msg: types.Message):
    await msg.answer("Marhamat Id va name yuboring")
    await AddState.add_user1.set()


@dp.message_handler(state=AddState.add_user1)
async def add_us(msg: types.Message, state: FSMContext):
    try:
        message = msg.text.split()
        id = message[0]
        name = message[1]
        try:
            db.add_user(id=id, name=name)
            await state.finish()
            await msg.answer("Foydalanuvchi bazaga qo'shildi")
        except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=982935447, text=err)
            await state.finish()
    except:
        await msg.reply("Nimadur xato ketti")
        await state.finish()







             