import requests 

from Victor import victor

from pyrogram import filters
from pyrogram.types import Message

@victor.on_message(filters.command("ud", ".") & filters.me)
async def ud(_, message: Message):
    if len(message.text.split()) == 1:
        await message.edit("Usage: `ud example`")
        return
            
    text = message.text.split(None, 1)[1]
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()

    try:
        reply_text = f'**{text}**\n\n{results["list"][0]["definition"]}\n\n__{results["list"][0]["example"]}__'
    except:
        reply_text = "No results found."

    await message.edit(reply_text)