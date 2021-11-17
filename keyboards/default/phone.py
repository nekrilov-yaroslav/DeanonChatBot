from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱phone number", request_contact=True)
        ]
    ],
    resize_keyboard=True
)
