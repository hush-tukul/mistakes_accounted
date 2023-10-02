import operator

from aiogram.enums import ParseMode, ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import (
    Select,
    Column,
    WebApp,
    SwitchTo,
    Row,
    Back,
    Cancel,
    Group,
)
from aiogram_dialog.widgets.media import StaticMedia, DynamicMedia
from aiogram_dialog.widgets.text import Format, Const

from tgbot.dialogs.getters import (
    gate_1_getter,
    gate_2_getter,
    gate_3_getter,
    main_menu,
    menu_sections_getter,
    section_photo,
    waiter_call_getter,
)
from tgbot.dialogs.setters import (
    to_gate_2,
    to_gate_3,
    gate_to_main,
    to_main_option,
    to_menu_sections_photo,
    admin_add_photo,
    to_waiter_reply,
    to_feedback_reply,
)
from tgbot.dialogs.states import (
    GateMenu,
    MainMenu,
    MenuSections,
    Admin,
    Waiter,
    Feedback,
)


def gates_windows():
    return [
        Window(
            StaticMedia(
                #url="https://telegra.ph//file/16de46d2de57505dedfd1.jpg", #futurecityimage
                url="https://telegra.ph//file/6137caf1dd9ef8fe2c200.jpg"
            ),
            Format("{gate_1_title}"),
            Column(
                Select(
                    Format("{item[0]}"),
                    id="gate_1",
                    item_id_getter=operator.itemgetter(1),
                    items="gate_1_buttons",
                    on_click=to_gate_2,
                ),
            ),
            parse_mode=ParseMode.HTML,
            state=GateMenu.gate_1,
            getter=gate_1_getter,
        ),
        Window(
            Format("{gate_2_title}"),
            Column(
                Select(
                    Format("{item[0]}"),
                    id="gate_2",
                    item_id_getter=operator.itemgetter(1),
                    items="gate_2_buttons",
                    on_click=to_gate_3,
                ),
            ),
            parse_mode=ParseMode.HTML,
            state=GateMenu.gate_2,
            getter=gate_2_getter,
        ),
        Window(
            Format("{gate_3_title}"),
            MessageInput(gate_to_main, ContentType.TEXT),
            parse_mode=ParseMode.HTML,
            state=GateMenu.gate_3,
            getter=gate_3_getter,
        ),
    ]


def main_windows():
    return [
        Window(
            StaticMedia(url="https://telegra.ph//file/0a899a91b7084ff6d4e64.jpg"),
            Format("{title}"),
            Column(
                # SwitchTo()
                Select(
                    Format("{item[0]}"),
                    id="menu",
                    item_id_getter=operator.itemgetter(1),
                    items="main_menu",
                    on_click=to_main_option,
                ),
                WebApp(
                    Const("🚚 Delivery 🚚"), Const("https://staskazakov.com/restaraunt/")
                ),
            ),
            parse_mode=ParseMode.HTML,
            state=MainMenu.main,
            getter=main_menu,
        )
    ]


def sections_windows():
    return [
        Window(
            StaticMedia(url="https://telegra.ph//file/0a899a91b7084ff6d4e64.jpg"),
            Format("{title}"),
            Row(
                Select(
                    Format("{item[0]}"),
                    id="menu_sections_1",
                    item_id_getter=operator.itemgetter(1),
                    items="menu_sections_1",
                    on_click=to_menu_sections_photo,
                ),
            ),
            Row(
                Select(
                    Format("{item[0]}"),
                    id="menu_sections_2",
                    item_id_getter=operator.itemgetter(1),
                    items="menu_sections_2",
                    on_click=to_menu_sections_photo,
                ),
            ),
            Row(
                Select(
                    Format("{item[0]}"),
                    id="menu_sections_3",
                    item_id_getter=operator.itemgetter(1),
                    items="menu_sections_3",
                    on_click=to_menu_sections_photo,
                ),
            ),
            Row(
                Select(
                    Format("{item[0]}"),
                    id="menu_sections_4",
                    item_id_getter=operator.itemgetter(1),
                    items="menu_sections_4",
                    on_click=to_menu_sections_photo,
                ),
            ),
            Cancel(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=MenuSections.menu_sections,
            getter=menu_sections_getter,
        ),
        Window(
            DynamicMedia("section_photo"),
            Back(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=MenuSections.section_photo,
            getter=section_photo,
        ),
    ]


def admin_windows():
    return [
        Window(
            Const("🕹️Admin panel🕹️"),
            SwitchTo(
                Const("➕ Add photo ➕"), id="add_photo", state=Admin.admin_add_photo
            ),
            Cancel(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=Admin.admin_panel,
        ),
        Window(
            Const("➕ Add item ➕"),
            Const("\n\nPlease send a picture"),
            MessageInput(admin_add_photo, ContentType.PHOTO),
            Back(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=Admin.admin_add_photo,
        ),
    ]


def waiter_windows():
    return [
        Window(
            StaticMedia(url="https://telegra.ph//file/4f87cb041876182662c0e.jpg"),

            Const("🤵 Waiter 🤵"),
            Const("Please choose Your table🍽️ number: "),
            Group(
                Select(
                    Format("{item[0]}"),
                    id="table_list",
                    item_id_getter=operator.itemgetter(1),
                    items="table_list",
                    on_click=to_waiter_reply,
                ),
                width=3,
            ),
            Cancel(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=Waiter.waiter_call,
            getter=waiter_call_getter,
        ),
        Window(
            StaticMedia(url="https://telegra.ph//file/073d7dc4e437f69212086.jpg"),
            Const("Thank you for using the waiter call through the bot 🤖"
                  "\nYour waiter is on his way 🏃‍♂️"),
            Cancel(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=Waiter.waiter_reply,
        ),

    ]


def feedback_windows():
    return [
        Window(
            StaticMedia(url="https://telegra.ph//file/f2ee48efd1e945dc4edde.jpg"),
            Const("📢 Feedback | Contact 📞"),
            Const("Please provide Your feedback below: "
                  "\n(Or You can contact directly with Us "
                  "- https://t.me/choose_your_bots)"),
            MessageInput(to_feedback_reply, ContentType.TEXT),
            Cancel(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=Feedback.feedback,

        ),
        Window(
            StaticMedia(url="https://telegra.ph//file/6ca79c58df2dd897025f4.jpg"),
            Const(
                "We sincerely appreciate your valuable feedback🙏"
                "\nThank you for Your opinion👍"
            ),
            Cancel(Const("Back")),
            parse_mode=ParseMode.HTML,
            state=Feedback.feedback_reply,
        ),
    ]