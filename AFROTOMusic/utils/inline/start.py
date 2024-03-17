from pyrogram.types import InlineKeyboardButton

import config
from AFROTOMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
          
        ],
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text="رمضان كريم", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="قناة السورس", url=f"https://t.me/FFFH0"),
        ],
        [
         
            InlineKeyboardButton(
                text="𝐊𝒆𝒗𝒊𝒏 𝐒𝒐𝒓𝒄𝒆♪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="المطور", user_id=config.OWNER_ID),
            
        ],
         [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text=" رمضان كريم", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="قناة السورس", url=f"https://t.me/FFFH0"),
        ],
        [
         
            InlineKeyboardButton(
                text="𝐊𝒆𝒗𝒊𝒏 𝐒𝒐𝒓𝒄𝒆♪",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons
