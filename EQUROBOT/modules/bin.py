from pyrogram import filters
from EQUROBOT import app, safone

@app.on_message(filters.command(["bin"], [".", "", "!", "/"]))
async def check_bin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**Hey, please give me any numeric BIN query.**"
        )
    
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
    
    aux = await message.reply_text("<b>Aah, wait, give me some time...</b>")
    
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>Oops, buddy, wrong format. Give me BIN in valid format.</b>")
    
    try:
        resp = await safone.bininfo(bin)
        await aux.edit(f"""
<b> 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅</b>
<b>┏━◆</b>
<b>┣〖🏦 ʙᴀɴᴋ</b> ⇾<tt>{resp.bank}</tt></b>
<b>┣〖💳 ʙɪɴ</b> ⇾<tt>{resp.bin}</tt></b>
<b>┣〖🏡 ᴄᴏᴜɴᴛʀʏ</b> ⇾<tt>{resp.country}</tt></b>
<b>┣〖🇮🇳 ғʟᴀɢ</b> ⇾<tt>{resp.flag}</tt></b>
<b>┣〖🧿 ɪsᴏ</b> ⇾<tt>{resp.iso}</tt></b>
<b>┣〖⏳ ʟᴇᴠᴇʟ</b> ⇾<tt>{resp.level}</tt></b>
<b>┣〖🔴 ᴘʀᴇᴘᴀɪᴅ</b> ⇾<tt>{resp.prepaid}</tt></b>
<b>┣〖🆔 ᴛʏᴘᴇ</b> ⇾<tt>{resp.type}</tt></b>
<b>┣〖ℹ️ ᴠᴇɴᴅᴏʀ</b> ⇾<tt>{resp.vendor}</tt></b>
<b>┗━━━◆</b>
""")
    except Exception as e:
        print(f"Error fetching BIN info: {e}")
        return await aux.edit("**🚫 BIN not recognized. Please enter a valid BIN.**")
