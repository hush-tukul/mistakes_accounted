import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from tgbot.dialogs.states import GateMenu

logger = logging.getLogger(__name__)
user_router = Router()


@user_router.message(CommandStart())
async def user_start(m: Message, dialog_manager: DialogManager):
    logger.info("You are in user_start")
    await dialog_manager.start(
        state=GateMenu.gate_1,
        mode=StartMode.RESET_STACK,
    )
