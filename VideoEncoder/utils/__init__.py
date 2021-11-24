from pyrogram import filters
from pyrogram.errors import RPCError

from .. import app as a
from . import buttons, ffmpeg, progress, task


@a.on_message(filters.command('so' 'ur' 'ce'))
async def g_s(_, message):
    try:
        await message.reply(text="prrrrr", reply_markup=buttons.output)
    except RPCError:
        pass
