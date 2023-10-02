from aiogram_dialog import Dialog

from tgbot.dialogs.windows import (
    gates_windows,
    main_windows,
    sections_windows,
    admin_windows,
    waiter_windows,
    feedback_windows,
)


def bot_menu_dialogs():
    return [
        Dialog(*gates_windows()),
        Dialog(*main_windows()),
        Dialog(*sections_windows()),
        Dialog(*admin_windows()),
        Dialog(*waiter_windows()),
        Dialog(*feedback_windows()),
    ]