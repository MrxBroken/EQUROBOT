from pyrogram import filters
from EQUROBOT import app, safone



@app.on_message(filters.command(["bin"], [".", "", "!", "/"]))
async def check_bin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**ʜᴇʏ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ᴀɴʏ ɴᴜᴍʙᴇʀɪᴄ ʙɪɴ ǫᴜᴇʀʏ.\n𝗕𝗬 ➤𝗠𝗥 𝗫 𝗕𝗥𝗢𝗞𝗘𝗡**"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>ᴀᴀʜ ᴡᴀɪᴛ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>ᴏᴏᴘs ʙᴜᴅᴅʏ ᴡʀᴏɴɢ ғᴏʀᴍᴀᴛ ɢɪᴠᴇ ᴍᴇ ʙɪɴ ɪɴ ᴠᴀʟɪᴅ ғᴏʀᴍᴀᴛ.</b>")
    try:
        resp = await safone.bininfo(bin)
        await aux.edit(f"""
<b> 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅</b>
<b>┏━◆</b>
<b>┣〖🏦 ʙᴀɴᴋ</b> ⇾<tt>{resp.bank}</tt>
<b>┣〖💳 ʙɪɴ</b> ⇾<tt>{resp.bin}</tt>
<b>┣〖🏡 ᴄᴏᴜɴᴛʀʏ</b> ⇾<tt>{resp.country}</tt>
<b>┣〖🇮🇳 ғʟᴀɢ</b> ⇾<tt>{resp.flag}</tt>
<b>┣〖🧿 ɪsᴏ</b> ⇾<tt>{resp.iso}</tt>
<b>┣〖⏳ ʟᴇᴠᴇʟ</b> ⇾<tt>{resp.level}</tt>
<b>┣〖🔴 ᴘʀᴇᴘᴀɪᴅ</b> ⇾<tt>{resp.prepaid}</tt>
<b>┣〖🆔 ᴛʏᴘᴇ</b> ⇾<tt>{resp.type}</tt>
<b>┣〖ℹ️ ᴠᴇɴᴅᴏʀ</b> ⇾<tt>{resp.vendor}</tt>
<b>┗━━━◆</b>
"""
        )
    except:
        return await aux.edit("**🚫 ʙɪɴ ɴᴏᴛ ʀᴇᴄᴏɢɴɪᴢᴇᴅ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ʙɪɴ.**\n𝗕𝗬 ➤𝗠𝗥 𝗫 𝗕𝗥𝗢𝗞𝗘𝗡")
