import importlib

from Victor import victor, LOGGER
from Victor.plugins import ALL_MODULES

from pyrogram import filters
from pyrogram.types import Message

IMPORTED = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("Victor.plugins." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")


@victor.on_message(filters.command("start", ".") & filters.me)
async def start(_, message: Message):
    txt = "I am succesfully running! \n\nPowered by @Wrecked_X_Union"
    await message.edit(txt)


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    victor.run()