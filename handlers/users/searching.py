from aiogram import types

from loader import dp


@dp.message_handler(text="Здійснити пошук 🔎")
async def start_search(message: types.Message):
    await message.answer(f"Привіт")
