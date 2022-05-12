import asyncio

from Victor import victor

from pyrogram import filters
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from pyrogram.types import Message

@victor.on_message(filters.command("setpic", ".") & filters.me)
async def setpic(_, message: Message):
    if message.chat.type in ["group", "supergroup"]:

        admins = await victor.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await victor.get_me()

        if me.id in admin_ids:

            my_permissions = None

            for user in admins:
                if user.user.id == me.id:
                    my_permissions = user

            if my_permissions and my_permissions.can_change_info:

                if message.reply_to_message and message.reply_to_message.media:
                    file_id = message.reply_to_message.photo.file_id
                    await victor.set_chat_photo(
                        chat_id=message.chat.id, photo=file_id
                    )
                    await message.edit(
                        f"`{message.chat.type.title()} picture has been set.`"
                    )
                    return
                else:
                    await message.edit(
                        f"`Please reply to a message with a photo to set it as {message.chat.type} picture.`"
                    )
            else:
                await message.edit("`I lack the permissions to do this...`")
        else:
            await message.edit("`I am not an admin here.`")
    else:
        await message.edit("`This is not a place where I can change the picture.`")

    await asyncio.sleep(3)
    await message.delete()

@victor.on_message(filters.command("rmpic", ".") & filters.me)
async def rmpic(_, message: Message):
    if message.chat.type in ["group", "supergroup"]:

        admins = await victor.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await victor.get_me()

        if me.id in admin_ids:

            my_permissions = None

            for user in admins:
                if user.user.id == me.id:
                    my_permissions = user

            if my_permissions and my_permissions.can_change_info:
                await victor.delete_chat_photo(chat_id=message.chat.id)

                await message.edit(
                    f"`{message.chat.type.title()} picture has been deleted`"
                )

            else:
                await message.edit("`I lack the permissions to do this...`")

        else:
            await message.edit("`I am not an admin here.`")

    else:
        await message.edit("`This is not a place where I can do this.")

    await asyncio.sleep(3)
    await message.delete()
