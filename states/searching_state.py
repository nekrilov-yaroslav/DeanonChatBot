from aiogram.dispatcher.filters.state import StatesGroup, State


class Searching(StatesGroup):
    login = State()
    search = State()
