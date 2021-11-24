from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .. import sudo_users

output = InlineKeyboardMarkup([
    [InlineKeyboardButton("Happy", url="t.me/mwklinks")]
])

async def check_user(message):
     await message.reply(text="OkDa Started")
        return None
