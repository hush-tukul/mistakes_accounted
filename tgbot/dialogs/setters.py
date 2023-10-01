import logging
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from tgbot.dialogs.states import GateMenu, MainMenu, MenuSections, Waiter, Сontact

logger = logging.getLogger(__name__)

async def to_gate_2(
    callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logger.info("You are in to_gate_2")
    logger.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(source=button)
    await dialog_manager.switch_to(GateMenu.gate_2)


async def to_gate_3(
    callback: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logger.info("You are in to_gate_3")
    logger.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(source=button)
    await dialog_manager.switch_to(GateMenu.gate_3)


async def gate_to_main(
    m: Message, input: MessageInput, dialog_manager: DialogManager
):
    logger.info("You are in gate_3_reply")
    date = m.text
    logging.info(f"button pressed: {date}")
    await dialog_manager.start(MainMenu.main)

async def to_main_option(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logger.info("You are in main_menu")
    logger.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(callback_id=c.id)
    g = {
        "menu": MenuSections.menu_sections,
        "waiter": Waiter.waiter_call,
        "contact": Сontact.contact_feedback,
        #"admin_panel": States.admin_panel_state,
    }
    await dialog_manager.start(g[button])


