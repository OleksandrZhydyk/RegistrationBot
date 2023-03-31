from aiogram.dispatcher.filters.state import State, StatesGroup


class AuthStates(StatesGroup):
    start_register = State()
    username = State()
    password = State()
    confirm_password = State()
    registration = State()
