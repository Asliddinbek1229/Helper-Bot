from loader import dp, bot
from aiogram.types import message
from checkWord import get_available, checkWords, trans_matches

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.kril_latin_keyboard import check_kb
from keyboards.default.menuKeyboards import menuKeyboard

from data.config import KEY

from states.imlo_state import Krill_LotinState

@dp.message_handler(Text("✅ So'zlarni tekshirish"), state=None)
async def started(msg: Message):
    await msg.delete()
    await msg.answer(
        "<b>Tekshirish uchun so'zlarni quyidagi tartibda yuboring</b>\n\nYakka holatda\n<i>Olma</i>\nBir nechta so'zlarni vergul bilan ajratib\n"
        "<i>Olma, anor, behi, nok, .... </i>"
    )
    await Krill_LotinState.FIRSTstate.set()

@dp.message_handler(state=Krill_LotinState.FIRSTstate)
async def response(msg: Message, state: FSMContext):
    for messi in KEY:
        if msg.text == messi:
            await state.finish()
            return
    await bot.delete_message(msg.from_user.id, msg.message_id-1)
    message = msg.text
    msg_list = message.split()
    for s in msg_list:
        if ',' in s:
            sz = s.replace(',', '')
            word = sz
            words = await checkWords(word)
            get = await get_available(words)
            if get:
                await msg.answer(f"✅ {word}")
            else:
                related = await trans_matches(words)
                sozlar = {}
                sozlar['word'] = f"❌ {word}"
                sozlar['words'] = "\n".join(related)
                await msg.answer(f"{sozlar['word']} \n{sozlar['words']}")
        elif '.' in s:
            sz = s.replace('.', '')
            word = sz
            words = await checkWords(word)
            get = await get_available(words)
            if get:
                await msg.answer(f"✅ {word}")
            else:
                related = await trans_matches(words)
                sozlar = {}
                sozlar['word'] = f"❌ {word}"
                sozlar['words'] = "\n".join(related)
                await msg.answer(f"{sozlar['word']} \n{sozlar['words']}")

        else:
            word = s
            words = await checkWords(word)
            get = await get_available(words)
            if get:
                await msg.answer(f"✅ {word}")
            else:
                related = await trans_matches(words)
                sozlar = {}
                sozlar['word'] = f"❌ {word}"
                sozlar['words'] = "\n".join(related)
                await msg.answer(f"{sozlar['word']} \n{sozlar['words']}")
                
    await msg.answer("Yana so'zlarni tekshirasizmi?", reply_markup=check_kb)


@dp.callback_query_handler(state=Krill_LotinState.FIRSTstate, text='yes')
async def yana_tek(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer(
        "<b>Tekshirish uchun so'zlarni quyidagi tartibda yuboring</b>\n\nYakka holatda\n<i>Olma</i>\nBir nechta so'zlarni vergul bilan ajratib\n"
        "<i>Olma, anor, behi, nok, .... </i>"
    )
    await call.answer()


@dp.callback_query_handler(state=Krill_LotinState.FIRSTstate, text="ortga")
async def back_check(call: CallbackQuery, state: FSMContext):
    # await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Quyidagi tugmalardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    await call.answer()
    await state.finish()
