import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import StartMode, DialogManager

from tgbot.dialogs.states import GateMenu
from tgbot.filters.admin import AdminFilter


logger = logging.getLogger(__name__)
admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(m: Message, dialog_manager: DialogManager):
    logger.info("You are in admin_start")

    await m.reply("Hello admin! 👋😎", parse_mode="HTML")
    await dialog_manager.start(
        state=GateMenu.gate_1,
        mode=StartMode.RESET_STACK,
    )



