from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗺Location", request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
