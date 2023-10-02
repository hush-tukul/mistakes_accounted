from aiogram.fsm.state import StatesGroup, State


class GateMenu(StatesGroup):
    gate_1 = State()
    gate_2 = State()
    gate_3 = State()


class MainMenu(StatesGroup):
    main = State()


class MenuSections(StatesGroup):
    menu_sections = State()
    section_photo = State()

class Waiter(StatesGroup):
    waiter_call = State()
    waiter_reply = State()

class Feedback(StatesGroup):
    feedback = State()
    feedback_reply = State()


class Admin(StatesGroup):
    admin_panel = State()
    admin_add_photo = State()




