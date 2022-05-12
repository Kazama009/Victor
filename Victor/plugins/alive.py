import time

from platform import python_version

from Victor import victor, START_TIME, victor_version

from pyrogram import filters, __version__
from pyrogram.types import Message 


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@victor.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, message: Message):
    uptime = get_readable_time((time.time() - START_TIME))
    master = message.from_user.mention
    vicver = victor_version
    pyrover = __version__
    pyver = python_version()
    msg = f'''
**Victor is Successfully Running**
**✧✧ Master :** {master}
**✧✧ Uptime :** `{uptime}`
**✧✧ Victor :** `{vicver}`
**✧✧ Pyrogram :** `{pyrover}`
**✧✧ Python :** `{pyver}`
'''
    await message.edit(msg)