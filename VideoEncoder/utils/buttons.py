from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .. import sudo_users

output = InlineKeyboardMarkup([
    [InlineKeyboardButton("Developer", url="https://github.com/WeebTime/"),
     InlineKeyboardButton("Source", url="https://github.com/WeebTime/Video-Encoder-Bot")]
])

async def check_user(message):
    user_id = message.from_user.id
    if user_id in sudo_users:
        return 'Sudo'
    else:
        await message.reply(text="OkDa, Started")
        return None
