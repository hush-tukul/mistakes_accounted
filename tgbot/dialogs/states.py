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


class Сontact(StatesGroup):
    contact_feedback = State()
    contact_reply = State()




