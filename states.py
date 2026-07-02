from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    action = State()

    user_model = State()
    target_model = State()

    screen = State()
    battery = State()
    body = State()
    repair = State()

    contact = State()