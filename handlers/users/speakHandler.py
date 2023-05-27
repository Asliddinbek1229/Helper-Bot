from utils.oxforLookUp import getDefinitions
from googletrans import Translator

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from loader import dp, bot

from states.speakEngState import SpeakEngState
from keyboards.inline.speakKeyboard import speak_kb
from keyboards.default.menuKeyboards import menuKeyboard

from data.config import KEY



@dp.message_handler(Text("🗣 Speak English"), state=None)
async def started_speak(msg: Message, state: FSMContext):
    await msg.delete()
    await msg.answer(
        f"🤩 SpeakEnglish bo'limiga xush kelibsiz <b>{msg.from_user.full_name}</b> 🥳🥳🥳\n\n"
        f"<b>Bu qismda siz kiritgan so'zingizni Ingliz tilidagi ma'nolari hamda Ingliz tilidagi talaffuzini bilib olasiz</b>\n\n"
        f"⚠️ <b>Eslatma:</b> Kiritayotgan so'zingiz <i>Ingliz tilida</i> bo'lishi va <i>ko'plik</i> ma'nosini anglatmasligi kerak!!!\n\n"
        f"<b>Marhamat Inglizcha so'z kiriting 👇👇👇</b>"
    )
    await SpeakEngState.firstState.set()


@dp.message_handler(state=SpeakEngState.firstState)
async def speak_lets(msg: Message, state: FSMContext):
    for messi in KEY:
        if msg.text == messi:
            await state.finish()
            return
    await bot.delete_message(msg.from_user.id, msg.message_id-1)
    wait = await bot.send_message(chat_id=msg.chat.id, text="🔁 So'z tayyorlanmoqda...")
    word_id = msg.text
    if len(msg.text.split()) > 2:
        await msg.answer("Kiritilgan so'z 2 tadan ko'p bo'lmasligi kerak!!!")
    else:
        lookup = await getDefinitions(word_id)
        if lookup:
            await msg.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup['audio']:
                await msg.reply(lookup['audio'])
            else:
                await msg.reply("Bu so'zning audiosi mavjud emas!!!")

        else:
            await msg.reply(f"😕 Bunday so'z topilmadi!!!")
    await wait.delete()
    await msg.answer("SpeakEnglish bo'limidan yana foydalanasizmi?", reply_markup=speak_kb)

@dp.callback_query_handler(state=SpeakEngState.firstState, text='yes')
async def yana_tek(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer(
        "<b>Marhamat so'z yuboring!!!</b>"
    )
    await call.answer()


@dp.callback_query_handler(state=SpeakEngState.firstState, text="ortga")
async def back_check(call: CallbackQuery, state: FSMContext):
    # await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Quyidagi tugmalardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    await call.answer()
    await state.finish()
