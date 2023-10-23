from pyrogram.types import InlineKeyboardButton

from config import ABOUT_ME
from AMMusicV2 import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
         [
            InlineKeyboardButton(
                text="ᴘᴀʀᴛ ᴏꜰ ᴀᴍ ? ", url=f"https://t.me/AbhiModszYT_Return/302"
            ),
             InlineKeyboardButton(
                text="ᴀʙᴏᴜᴛ ᴍᴇ 🤭", url=f"{ABOUT_ME}"
            ),
        ],
    ]
    return buttons
