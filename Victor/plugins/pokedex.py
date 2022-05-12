import aiohttp

from pyrogram import filters
from pyrogram.types import Message

from Victor import victor 

@victor.on_message(filters.command("pokedex", ".") & filters.me)
async def PokeDex(_, message: Message):
    chat_id = message.chat.id
    
    if len(message.command) != 2:
        await message.edit("Use `.pokedex <pokemon>`")
        return

    pokemon = message.text.split(None, 1)[1]
    pokedex = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"

    async with aiohttp.ClientSession() as session:
        async with session.get(pokedex) as request:
            if request.status == 404:
                return await message.edit("Wrong Pokemon Name")

            result = await request.json()

            try:
                pokemon = result["name"]
                pokedex = result["id"]
                type = result["type"]
                poke_img = f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg"
                abilities = result["abilities"]
                height = result["height"]
                weight = result["weight"]
                gender = result["gender"]
                stats = result["stats"]
                description = result["description"]
                caption = f"""
**Pokemon:** `{pokemon}`
**Pokedex:** `{pokedex}`
**Type:** `{type}`
**Abilities:** `{abilities}`
**Height:** `{height}`
**Weight:** `{weight}`
**Gender:** `{gender}`
**Stats:** `{stats}`
**Description:** `{description}`"""
            except Exception as e:
                print(str(e))
                pass

            await victor.send_photo(chat_id=chat_id, photo=poke_img, caption=caption)
            await message.delete()