from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

search = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔒 Авторизуватися 🔓", request_contact=True)],
        [KeyboardButton(text="🔎 Здійснити пошук 🔎")]
    ],
    resize_keyboard=True
)
