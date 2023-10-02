import logging
import os
import secrets
from io import BytesIO
from typing import Any

import aiohttp
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from tgbot.dialogs.states import (
    GateMenu,
    MainMenu,
    MenuSections,
    Waiter,
    Admin,
    Feedback,
)
from tgbot.dialogs.telegraph import UploadedFile

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
        "contact": Feedback.feedback,
        "admin_panel": Admin.admin_panel,
    }
    await dialog_manager.start(g[button])


async def to_menu_sections_photo(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logger.info("You are in menu_sections_reply")
    logger.info(f"button pressed: {button}")
    dialog_manager.dialog_data.update(section_photo=button)
    await dialog_manager.switch_to(MenuSections.section_photo)


async def admin_add_photo(
    m: Message, input: MessageInput, dialog_manager: DialogManager
):
    logger.info("You are in admin_add_photo")
    item_photo = m.photo[-1].file_id
    downloaded_photo = await m.bot.download(item_photo, destination=BytesIO())
    form = aiohttp.FormData(quote_fields=False)
    form.add_field(secrets.token_urlsafe(8), downloaded_photo)
    new_session = aiohttp.ClientSession()
    response = await new_session.post(
        os.getenv("BASE_TELEGRAPH_API_LINK").format(endpoint="upload"),
        data=form
    )
    logger.info(response.url)
    json_response = await response.json()
    photo_url = [UploadedFile.model_validate(obj) for obj in json_response][0].link
    logger.info(f"photo_url: {photo_url}")
    await new_session.close()

    await m.answer(text="Photo was uploaded successfully!", parse_mode="HTML")
    await dialog_manager.back()


async def to_waiter_reply(
    c: CallbackQuery, widget: Any, dialog_manager: DialogManager, button: str
):
    logger.info("You are in to_waiter_reply")
    logger.info(f"button pressed: {button}")
    await c.answer(text="Thank you for using the waiter call through the bot 🤖"
                        "\nYour waiter is on his way 🏃‍♂️",
                        cache_time=5)
    await dialog_manager.switch_to(Waiter.waiter_reply)


async def to_feedback_reply(
        m: Message, input: MessageInput, dialog_manager: DialogManager
):
    logger.info("You are in to_feedback_reply")
    await dialog_manager.switch_to(Feedback.feedback_reply)

