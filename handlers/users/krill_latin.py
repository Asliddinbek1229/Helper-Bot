from krill_latin import krill_latin
from states.krillState import KrillState

from loader import dp, bot

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboards.inline.transKrilLatin import K_L_kb
from keyboards.default.menuKeyboards import menuKeyboard

from data.config import KEY



@dp.message_handler(Text("♻️ Krill-lotin"), state=None)
async def translate(msg: Message):
    await msg.delete()
    await msg.answer(
        f"🤩 Krill_latin bo'limiga xush kelibsiz <b>{msg.from_user.full_name}</b> 🥳🥳🥳\n\n"
        f"<b>Bu qismda siz yuborgan matningiz <i>krillchada</i> bo'lsa <i>lotinchaga</i>\n"
        f"Aks holda <i>lotinchadan</i> <i>krillchaga</i> o'tkazib beradi</b>\n\n"
        f"<b>Marhamat matn yuboring</b>"
    )
    await KrillState.firstState.set()

@dp.message_handler(state=KrillState.firstState)
async def krill_trans(msg: Message, state: FSMContext):
    for messi in KEY:
        if msg.text == messi:
            await state.finish()
            return
    await bot.delete_message(msg.from_user.id, msg.message_id-1)
    trans = await krill_latin(msg.text)
    await msg.answer(trans)
    await msg.answer("Yana tarjima qilishni hohlaysizmi?", reply_markup=K_L_kb)


@dp.callback_query_handler(text='yes', state=KrillState.firstState)
async def yes_no(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer(
        "<b>Marhamat matn yuboring!!!</b>"
    )
    await call.answer()


@dp.callback_query_handler(state=KrillState.firstState, text="ortga")
async def back_check(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Quyidagi tugmalardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    await call.answer()
    await state.finish()


