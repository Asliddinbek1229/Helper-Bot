from aiogram.dispatcher.filters.state import StatesGroup, State

class AdminState(StatesGroup):
    OneState = State()
    textState = State()