import operator

from aiogram.enums import ParseMode, ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Column, WebApp
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Format, Const

from tgbot.dialogs.getters import gate_1_getter, gate_2_getter, gate_3_getter, main_menu
from tgbot.dialogs.setters import to_gate_2, to_gate_3, gate_to_main, to_main_option
from tgbot.dialogs.states import GateMenu, MainMenu


def gates_window():
    return [
        Window(
            StaticMedia(
                url="https://telegra.ph//file/16de46d2de57505dedfd1.jpg",
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
        )

    ]


def main_window():
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
                WebApp(Const("🚚 Delivery 🚚"), Const("https://staskazakov.com/restaraunt/")),
            ),
            parse_mode=ParseMode.HTML,
            state=MainMenu.main,
            getter=main_menu,
        )
    ]


def sections_window():
    return [

    ]