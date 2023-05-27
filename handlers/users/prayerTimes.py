from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.muslimsalat import prayer_times
from utils.datetimes import todays_date
from keyboards.inline.pr_keyboard import prayer_keyboard
from keyboards.default.menuKeyboards import menuKeyboard
from states.prayerT import PT_state

from data.config import KEY

from aiogram.dispatcher.filters import Text


@dp.message_handler(Text("🕋 Namoz vaqtlarini ko'rish"), state=None)
async def one(msg: types.Message, state: FSMContext):
    await msg.delete()
    await msg.answer("Namoz vaqtlarini ko'rish uchun <b>ko'rish</b> tugmasini bosing!!!", reply_markup=prayer_keyboard)
    await PT_state.view_PT.set()


@dp.message_handler(state=PT_state.view_PT, content_types='text')
async def error(msg: types.Message, state: FSMContext):
    for messi in KEY:
        if msg.text == messi:
            await state.finish()
            return
    await msg.answer("Iltimos <b>Ko'rish</b> yoki <b>Ortga</b> tugmalaridan birini tanlang!!!", reply_markup=prayer_keyboard)


@dp.callback_query_handler(text='view', state=PT_state.view_PT)
async def prayer_t(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    times = await prayer_times()
    p_times = ""
    today = await todays_date()
    today = str(today)
    p_times += f"🗓 <b>Bugungi sana: {today}</b>\n"

    for p, t in times.items():
        time = f"<b>{p}</b>: {t}"
        p_times += f"\n{time}"
    await call.message.answer(p_times)
    await call.answer(cache_time=60)
    await state.finish()


@dp.callback_query_handler(state=PT_state.view_PT, text='back')
async def back_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Quyidagilardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    await call.answer()
    await state.finish()
