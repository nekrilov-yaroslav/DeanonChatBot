from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗺location", request_location=True)
        ]
    ],
    resize_keyboard=True
)
