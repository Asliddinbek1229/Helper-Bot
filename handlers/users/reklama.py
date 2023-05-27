from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from states.adminState import AdminState
from keyboards.inline.reklamaKB import rek_kb

from loader import dp, bot

from handlers.users.start import users





@dp.message_handler(chat_id=982935447, commands=['reklama'])
async def reklama(msg: Message):
    await msg.answer(
        "Reklamani qaysi ko'rinishda yubormoqchisiz?", reply_markup=rek_kb
    )
    await AdminState.OneState.set()

@dp.callback_query_handler(text='text', state=AdminState.OneState)
async def send_text(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Matn yuboring")
    await call.answer()
    await AdminState.textState.set()

@dp.message_handler(state=AdminState.textState)
async def send_matn(msg: Message, state: FSMContext):
    reklama = msg.text
    for user_id in users:
        await bot.send_message(chat_id=user_id, text=reklama)
    await msg.answer("Xabaringiz foydalanuvchilariga yetkazildi")
    await state.finish()

    