

from pyrogram import Client, filters

from .. import data, sudo_users
from ..utils.tasks import handle_task
from ..utils.buttons import check_user

video_mimetype = [
    "video/x-flv",
    "video/mp4",
    "application/x-mpegURL",
    "video/MP2T",
    "video/3gpp",
    "video/quicktime",
    "video/x-msvideo",
    "video/x-ms-wmv",
    "video/x-matroska",
    "video/webm",
    "video/x-m4v",
    "video/quicktime",
    "video/mpeg",
    "document/mkv",
    "document/mp4",
    "video/mkv"
]


@Client.on_message(filters.incoming & (filters.video | filters.document))
async def encode_video(app, message):
    check = await check_user(message)
    if check is None:
        return
    else: 
        pass
    if message.document:
        if not message.document.mime_type in video_mimetype:
            return
    await message.reply_text("<code>Added to queue...</code>")
    data.append(message)
    if len(data) == 1:
        await handle_task(message)
