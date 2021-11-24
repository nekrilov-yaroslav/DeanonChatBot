from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import back_del
from loader import dp, db, bot
from states import Searching


@dp.callback_query_handler(text="back_del", state=Searching.search)
async def show_categories(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)


@dp.message_handler(text="🔎 Здійснити пошук 🔎")
async def start_search(message: types.Message):
    await message.answer(f"Нажаль Ви не авторизовані.\nПройдіть авторизацію для початку пошуку.")


@dp.message_handler(text="🔎 Здійснити пошук 🔎", state=Searching.login)
async def start_search(message: types.Message):
    await message.answer(f"Для здійснення пошуку надішліть текстовим повідомленням номер телефону.")
    await Searching.search.set()


@dp.message_handler(text="🔎 Здійснити пошук 🔎", state=Searching.search)
async def start_search(message: types.Message):
    await message.answer(f"Для здійснення пошуку надішліть текстовим повідомленням номер телефону.")


@dp.message_handler(state=Searching.search)
async def search(message: types.Message):
    x = await db.select_phone(phone_number=message.text)
    result = ''
    for i in range(len(x)):
        last_name = x[i].get('last_name')
        first_name = x[i].get('first_name')
        father_name = x[i].get('father_name')
        date_of_birth = x[i].get('date_of_birth')
        email = x[i].get('email')
        phone_number = x[i].get('phone_number')
        y = f"<b>{last_name} {first_name} {father_name}</b>\n🚼 {date_of_birth}\n🌐Електронна пошта: {email}" \
            f"\n📞 {phone_number}"
        result += y
    await message.answer(f"{result}", reply_markup=back_del)

