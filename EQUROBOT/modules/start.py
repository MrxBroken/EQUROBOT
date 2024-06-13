from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, OWNER_ID
from pyrogram.types import InlineKeyboardButton as ib
import asyncio
from EQUROBOT import app


START_TEXT = """
ʜɪ , {first}

ɪ ᴀᴍ , [☾𝗘𝗾𝘂𝗿𝗼𝗕𝗼𝘁☽](http://t.me/EQURO_BOT) 
ʏᴏᴜʀ ᴀɪ ᴄᴏᴍᴘᴀɴɪᴏɴ. 
ʟᴇᴛ'ꜱ ᴄʜᴀᴛ ᴀɴᴅ ᴇxᴘʟᴏʀᴇ 
ᴛʜᴇ ᴅᴇᴘᴛʜꜱ ᴏꜰ ᴄᴏɴᴠᴇʀꜱᴀᴛɪᴏɴ ᴛᴏɢᴇᴛʜᴇʀ! 
ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀꜱᴋ ᴍᴇ ᴀɴʏᴛʜɪɴɢ ᴏʀ ꜱʜᴀʀᴇ ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛꜱ. 
ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ʟɪꜱᴛᴇɴ ᴀɴᴅ ᴇɴɢᴀɢᴇ ɪɴ ᴍᴇᴀɴɪɴɢꜰᴜʟ ᴅɪꜱᴄᴜꜱꜱɪᴏɴꜱ ᴡɪᴛʜ ʏᴏᴜ ‣ \n @BROKENXNETWORK\n 𝐁𝐘 [➤𝗠𝗥 𝗫 𝗕𝗥𝗢𝗞𝗘𝗡](https://t.me/mrbrokn)"
"""



@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("⦿𝐀𝐃𝐃 𝐌𝐄⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("⦿𝐆𝐑𝐎𝐔𝐏⦿", url=f"https://t.me/brokenxnetwork"),
            InlineKeyboardButton("⦿𝐎𝐖𝐍𝐄𝐑⦿", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://graph.org/file/6efbbb4d9e43c0572b4f4.jpg",
        caption=START_TEXT,
        reply_markup=reply_markup
    )
