import nekos

from Victor import victor

from pyrogram import filters
from pyrogram.types import Message

@victor.on_message(filters.command("neko", ".") & filters.me)
async def neko(_, message: Message):
    await message.delete()
    target = "neko"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)

@victor.on_message(filters.command("hentai", ".") & filters.me)
async def hentai(_, message: Message):
    await message.delete()
    target = "hentai"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)

@victor.on_message(filters.command("feet", ".") & filters.me)
async def feet(_, message: Message):
    await message.delete()
    target = "feet"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)

@victor.on_message(filters.command("yuri", ".") & filters.me)
async def yuri(_, message: Message):
    await message.delete()
    target = "yuri"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)

@victor.on_message(filters.command("trap", ".") & filters.me)
async def trap(_, message: Message):
    await message.delete()
    target = "trap"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)

@victor.on_message(filters.command("funatari", ".") & filters.me)
async def funatari(_, message: Message):
    await message.delete()
    target = "funatari"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)

@victor.on_message(filters.command("boobs", ".") & filters.me)
async def boobs(_, message: Message):
    await message.delete()
    target = "boobs"
    pic = nekos.img(target)
    chat_id = message.chat.id
    await victor.send_photo(photo=pic, chat_id=chat_id)