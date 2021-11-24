


@Client.on_message(filters.command(['start']))
async def start_message(app, message):
    await message.reply(text="OkDa Started")
 
@Client.on_message(filters.command(['help']))
async def hlp_message(app, message):
    await message.reply(text="OkDa Helped")
 
