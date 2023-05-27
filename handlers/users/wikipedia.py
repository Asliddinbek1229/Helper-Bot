from utils.wikitest import sendWiki

from loader import dp, bot
from states.wikiState import WikiState
from keyboards.inline.wikiKeyboard import wiki_to
from keyboards.default.menuKeyboards import menuKeyboard

from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from data.config import KEY


@dp.message_handler(Text("🌐 Wikipedia"), state=None)
async def wiki_started(msg: Message):
    await msg.delete()
    await msg.answer(
        f"🤩 Wikipedia bo'limiga xush kelibsiz <b>{msg.from_user.full_name}</b> 🥳🥳🥳\n\n"
        f"<b>Bu qismda siz yuborgan maqolangiz asosida qiduruv <i>Wikipedia.uz</i> sayti orqali amalga oshadi.\n"
        f"Sizga kerakli bo'lgan maqolani qidirib, topib beradi</b>\n\n"
        f"<b>Marhamat maqola nomini yuboring</b>"
    )
    await WikiState.firsWiki.set()

@dp.message_handler(state=WikiState.firsWiki)
async def search_sum(msg: Message, state: FSMContext):
    for messi in KEY:
        if msg.text == messi:
            await state.finish()
            return
    wait = await bot.send_message(chat_id=msg.from_user.id, text='🚀 Maqola tayyorlanmoqda')
    await bot.delete_message(msg.from_user.id, msg.message_id-1)
    summary = await sendWiki(msg.text)
    await msg.answer(summary)
    await wait.delete()
    await msg.answer("Yana <b>Wikipedia</b> bo'limidan foydalanasizmi??", reply_markup=wiki_to)


@dp.callback_query_handler(text='yes', state=WikiState.firsWiki)
async def yana_wiki(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer(
        "<b>Marhamat maqola nomini yuboring!!!</b>"
    )
    await call.answer()


@dp.callback_query_handler(state=WikiState.firsWiki, text="ortga")
async def back_check(call: CallbackQuery, state: FSMContext):
    # await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Quyidagi tugmalardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    await call.answer()
    await state.finish()