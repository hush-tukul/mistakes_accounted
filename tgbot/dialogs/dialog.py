from aiogram_dialog import Dialog

from tgbot.dialogs.windows import gates_window, main_window


def bot_menu_dialogs():
    return [
        Dialog(*gates_window()),
        Dialog(*main_window()),
    ]