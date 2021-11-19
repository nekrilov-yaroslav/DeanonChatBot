from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱Phone number", request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
