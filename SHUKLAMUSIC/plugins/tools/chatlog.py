import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from SHUKLAMUSIC import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://files.catbox.moe/kq8gwp.jpg",
    "https://files.catbox.moe/tyijbe.jpg",
    "https://files.catbox.moe/6lywo3.jpg",
    "https://files.catbox.moe/2m61a9.jpg",
    "https://files.catbox.moe/c4jv3u.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"#𝗕𝗢𝗧_𝗔𝗗𝗗𝗘𝗗_𝗡𝗘𝗪_𝗚𝗥𝗢𝗨𝗣\n\n"
                f"____________________________________\n\n"
                f"◎ ᴄʜᴀᴛ ɴᴀᴍᴇ ▸: {chat.title}\n"
                f"◎ ᴄʜᴀᴛ ɪᴅ ▸: {chat.id}\n"
                f"◎ ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ▸ : @{chat.username}\n"
                f"◎ ᴄʜᴀᴛ ʟɪɴᴋ ▸: [ᴄʟɪᴄᴋ]({link})\n"
                f"◎ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ▸: {count}\n"
                f"◎ ᴀᴅᴅᴇᴅ ʙʏ ▸: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"#𝗦𝗘𝗘 𝗚𝗥𝗢𝗨𝗣#", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝗨𝗡𝗢𝗪𝗢𝗡 𝗨𝗦𝗘𝗥"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝗣𝗥𝗜𝗩𝗔𝗧𝗘"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝗟𝗘𝗙𝗧_𝗚𝗥𝗢𝗨𝗣</u></b> ❀\n\n𝗖𝗛𝗔𝗧 𝗧𝗜𝗧𝗟𝗘 : {title}\n\n𝗖𝗛𝗔𝗧 𝗜𝗗 : {chat_id}\n\n𝗥𝗘𝗠𝗢𝗩𝗘 𝗕𝗬 : {remove_by}\n\n𝗕𝗢𝗧 : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        
