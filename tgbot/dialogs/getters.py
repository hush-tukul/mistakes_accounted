import logging

from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment
from environs import Env

from infrastructure.database.repo.requests import RequestsRepo

logger = logging.getLogger(__name__)

env = Env()

async def gate_1_getter(
        dialog_manager: DialogManager, **kwargs
):
    logger.info("You are in profile_getter")
    gate_1_title = (
        "Welcome My Friend to the Restaurant-bot! 🍽️😃 We're ready to serve and help You with Your wishes. 🤖🛎️"
        "\nPlease answer some questions, We're so happy to get to know You better! 😊📝"
        "\n---------------------------------------------"
        "\nWhere from do You know about Us? 🌐🤔"
    )
    gate_1_buttons = [
        ("😄 Friends", "friends"),
        ("👍 Facebook", "facebook"),
        ("📷 Instagram", "instagram"),
        ("✉️ Telegram", "telegram"),
    ]
    return {
        "gate_1_title": gate_1_title,
        "gate_1_buttons": gate_1_buttons,
    }

async def gate_2_getter(
        dialog_manager: DialogManager, **kwargs
):
    gate_2_title = "Thank You🙏, and tell Us please," "\nHow can I address you??🤔"
    gate_2_buttons = [
        ("🕴️ Mr.", "mr"),
        ("💃 Miss/Mrs.", "miss_mrs"),
    ]
    return {
        "gate_2_title": gate_2_title,
        "gate_2_buttons": gate_2_buttons,
    }



async def gate_3_getter(
        dialog_manager: DialogManager, **kwargs
):
    gate_3_title = (
        "🎉 And last one...Promise😊" "\n🍰 We'll be happy to know when is Your Birthday?"
    )
    
    return {
        "gate_3_title": gate_3_title,
    }

async def main_menu(
        dialog_manager: DialogManager, **kwargs
):
    logger.info("You are in main_menu_inline")
    user_data = dialog_manager.middleware_data.get("user")
    logger.info(f"user_data: {user_data.user_id}")
    logger.info(f"user_data.user_id: {user_data.user_id}")
    title = "━━ 🍽️ Main Menu 🍽️ ━━"
    main_menu = [
        ("📝 Menu 📝", "menu"),
        ("👨‍🍳 Waiter 👨‍🍳", "waiter"),
        ("📢 Feedback | Contact 📞", "contact"),
        ("🕹️Admin panel🕹️", "admin_panel")
        if user_data.user_id in list(map(int, env.list("ADMINS")))
        else None,
    ]
    
    return {"title": title, "main_menu": main_menu if main_menu[3] else main_menu[:3]}





async def menu_sections_getter(
        dialog_manager: DialogManager, **kwargs
):
    logger.info("You are in menu_sections_inline")
    title = "━━ 📚 Menu Sections 📚 ━━"
    menu_sections = [
        ("🍽️ Starters 🍽️", "starters"),
        ("🥗 Salads 🥗", "salads"),
        ("🍲 Main Dishes 🍲", "main_dishes"),
        ("🍜 Soups 🍜", "soups"),
        ("🍣 Sushi 🍣", "sushi"),
        ("🍹 Cocktails 🍹", "cocktails"),
        ("🍺 Other drinks 🍺", "other_drinks"),
    ]
    
    return {
        "title": title,
        "menu_sections_1": menu_sections[:2],
        "menu_sections_2": menu_sections[2:4],
        "menu_sections_3": menu_sections[4:6],
        "menu_sections_4": menu_sections[6:],
    }



async def section_photo(
        dialog_manager: DialogManager, **kwargs
):
    logger.info("You are in menu_sections_inline")
    section_photo = dialog_manager.dialog_data.get("section_photo")
    menu = {
        "starters": "https://telegra.ph//file/d804cf0420321005602b2.jpg",
        "salads": "https://telegra.ph//file/7951a8916884fbcd998bf.jpg",
        "main_dishes": "https://telegra.ph//file/7914468bf7ad0b353739a.jpg",
        "soups": "https://telegra.ph//file/7daac15523621202a7f48.jpg",
        "sushi": "https://telegra.ph//file/7bdb178b0c883e1b704e0.jpg",
        "cocktails": "https://telegra.ph//file/9e257aa5023c3d09ed463.jpg",
        "other_drinks": "https://telegra.ph//file/e6d1edfe43a5780b8f68c.jpg",
    }
    return {
        "section_photo": MediaAttachment(ContentType.PHOTO, url=menu[section_photo]),
    }


async def waiter_call_getter(dialog_manager: DialogManager, **kwargs):
    logger.info("You are in waiter_call_getter")
    table_list = [
        ("1️⃣", "1"),
        ("2️⃣", "2"),
        ("3️⃣", "3"),
        ("4️⃣", "4"),
        ("5️⃣", "5"),
        ("6️⃣", "6"),
        ("7️⃣", "7"),
        ("8️⃣", "8"),
        ("9️⃣", "9"),
        ("🔟", "10"),
    ]

    return {
        "table_list": table_list,
    }
