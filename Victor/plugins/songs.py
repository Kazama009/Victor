import os
import requests
import aiohttp
import youtube_dl

from youtube_search import YoutubeSearch

from Victor import victor

from pyrogram import filters
from pyrogram.types import Message 

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@victor.on_message(filters.command("song", ".") & filters.me)
async def songs(_, message: Message):
    chat_id = message.chat.id
    query = ''

    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)

    m = await message.edit('`🔎 Finding the song...`')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        await m.edit(
            "✖️ Found Nothing. Sorry.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return

    await m.edit("`Downloading Song...`")

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        rep = f'🎙 **Title**: [{title[:35]}]({link})\n🎬 **Source**: YouTube\n⏱️ **Duration**: `{duration}`\n👁‍🗨 **Views**: `{views}`'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60

        await victor.send_audio(chat_id=chat_id, audio=audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        await m.delete()

    except Exception as e:
        await m.edit('❌ Error report it to @Retroginibots')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)