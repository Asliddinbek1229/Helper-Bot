import requests


from loader import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline.tarjimonKeyboard import trans_kb, back_to
from keyboards.default.menuKeyboards import menuKeyboard

from states.tarjimonState import TransState
from aiogram.dispatcher.filters import Text

from data.config import KEY

url = "https://google-translate105.p.rapidapi.com/v1/rapid/translate"


@dp.message_handler(Text("🔁 Tarjimon"), state=None)
async def first_trans(msg: Message, state: FSMContext):
    await msg.delete()
    await msg.answer("<b>Tarjima yo'nalishini tanlang</b>", reply_markup=trans_kb)
    await TransState.First.set()


@dp.callback_query_handler(text='uz_en', state=TransState.First)
async def uz_trans(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>Tarjima qilish uchun o'zbekcha so'z yuboring</b>")
    await TransState.UzState.set()
    await call.answer()

@dp.message_handler(state=TransState.UzState)
async def uz_tansl(msg: Message, state: FSMContext):
    for messi in KEY:
        if msg.text == messi:
            await state.finish()
            return
    wait = await bot.send_message(chat_id=msg.chat.id, text="🔁 Matn tarjima qilinmoqda...")
    payload = {
	    "text": msg.text,
	    "to_lang": "en",
	    "from_lang": "uz"
    }
    headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "X-RapidAPI-Key": "1c330a2f08msh848ab9829abc7ecp155179jsn3557bd392074",
	    "X-RapidAPI-Host": "google-translate105.p.rapidapi.com"
    }

    
    response = requests.post(url, data=payload, headers=headers)
    if 'message' in response.json():
        await msg.answer("❌ <b>Bunday so'z mavjud emas</b>\n\n"
                         "⚠️ <b>Eslatma:</b> \nSiz <b>uz-en</b> yo'nalishi tanlaganingizdan so'ng botga o'zbekcha so'z yuborishingiz kerak\n"
                         "Yoki to'g'ri so'z yuboring!!!")
        await wait.delete()
    else:
        await wait.delete()
        await msg.reply(response.json()['translated_text'])
        await msg.answer("Yana matn tarjima qilasizmi?", reply_markup=back_to)



@dp.callback_query_handler(text='yes', state=TransState.UzState)
async def repeat(call: CallbackQuery, state: FSMContext):
    # await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("<b>Tarjima qilish uchun o'zbekcha so'z yuboring</b>")
    await call.answer()

@dp.callback_query_handler(text='ortga', state=TransState.UzState)
async def ortga(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>Tarjima yo'nalishini tanlang</b>", reply_markup=trans_kb)
    await TransState.First.set()


@dp.callback_query_handler(text='orqaga', state=TransState.First)
async def back_menu(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("Quyidagi tugmalardan birini tanlang 👇👇👇", reply_markup=menuKeyboard)
    await call.answer()
    await state.finish()


@dp.callback_query_handler(text="en_uz", state=TransState.First)
async def en_trans(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>Tarjima qilish uchun inglizcha so'z yuboring</b>")
    await TransState.EnState.set()
    await call.answer()


@dp.message_handler(state=TransState.EnState)
async def en_transl(msg: Message, state: FSMContext):
    if msg.text in ['/start', '/help', "🎆 Rasm fonini olib tashlash", "🕋 Namoz vaqtlarini ko'rish", "🔁 Tarjimon", "✅ So'zlarni tekshirish", "🗣 Speak English", "🌐 Wikipedia", "♻️ Krill-lotin"]:
        await state.finish()
        return
    wait = await bot.send_message(chat_id=msg.chat.id, text="🔁 Matn tarjima qilinmoqda...")
    payload = {
	    "text": msg.text,
	    "to_lang": "uz",
	    "from_lang": "en"
    }
    headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "X-RapidAPI-Key": "1c330a2f08msh848ab9829abc7ecp155179jsn3557bd392074",
	    "X-RapidAPI-Host": "google-translate105.p.rapidapi.com"
    }

    
    response = requests.post(url, data=payload, headers=headers)
    if 'message' in response.json():
        await msg.answer("❌ <b>Bunday so'z mavjud emas</b>\n\n"
                         "⚠️ <b>Eslatma:</b> \nSiz <b>en-uz</b> yo'nalishi tanlaganingizdan so'ng botga o'zbekcha so'z yuborishingiz kerak\n"
                         "Yoki to'g'ri so'z yuboring!!!")
        await wait.delete()
    else:
        await wait.delete()
        await msg.reply(response.json()['translated_text'])
        await msg.answer("Yana matn tarjima qilasizmi?", reply_markup=back_to)


@dp.callback_query_handler(text='yes', state=TransState.EnState)
async def repeat(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup()
    await call.message.delete()
    await call.message.answer("<b>Tarjima qilish uchun inglizcha so'z yuboring</b>")
    await call.answer()

@dp.callback_query_handler(text='ortga', state=TransState.EnState)
async def ortga(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>Tarjima yo'nalishini tanlang</b>", reply_markup=trans_kb)
    await TransState.First.set()

    
    



