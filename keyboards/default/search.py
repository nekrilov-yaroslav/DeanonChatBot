from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

search = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Здійснити пошук 🔎")
        ]
    ],
    resize_keyboard=True
)
