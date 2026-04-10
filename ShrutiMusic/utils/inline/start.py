from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_11"],
                callback_data="about_page"
            )
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✙ ᴧᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⌯ ʜᴇʟᴘ ᴧηᴅ ᴄᴏᴍᴍᴧηᴅs ⌯",
                callback_data="help_page_1"
            )
        ],
        [
            InlineKeyboardButton(
                text="⌯ sᴜᴘᴘᴏꝛᴛ ⌯",
                url="https://t.me/CarelessxWorld"
            ),
            InlineKeyboardButton(
                text="⌯ ᴜᴘᴅᴧᴛᴇ ⌯",
                url="https://t.me/CarelessxCoder"
            )
        ],
        [
            InlineKeyboardButton(
                text="⌯ ᴍʏ ᴍᴀsᴛᴇʀ ⌯",
                user_id=config.OWNER_ID
            )
        ],
    ]
    return buttons

def about_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons

def owner_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_H_1"], url=config.INSTAGRAM),
            InlineKeyboardButton(text=_["S_H_2"], url=config.YOUTUBE),
        ],
        [
            InlineKeyboardButton(text=_["S_H_3"], url=config.GITHUB),
            InlineKeyboardButton(text=_["S_H_4"], url=config.DONATE),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper")
        ]
    ]
    return buttons


# ©️ Copyright Reserved - @NoxxOP  Nand Yaduwanshi

# ===========================================
# ©️ 2025 Nand Yaduwanshi (aka @NoxxOP)
# 🔗 GitHub : https://github.com/NoxxOP/ShrutiMusic
# 📢 Telegram Channel : https://t.me/ShrutiBots
# ===========================================


# ❤️ Love From ShrutiBots 
