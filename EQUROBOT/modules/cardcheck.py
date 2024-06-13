from pyrogram import filters
from EQUROBOT import app, safone

@app.on_message(filters.command(["ckc"], [".", "", "!", "/"]))
async def check_card(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**Hey, please provide a card number.**"
        )
    
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
    
    aux = await message.reply_text("<b>Checking the card, please wait...</b>")
    
    card_number = message.text.split(None, 1)[1]
    if len(card_number) < 12 or len(card_number) > 19:
        return await aux.edit("<b>Oops, buddy, wrong format. Please provide a valid card number.</b>")
    
    bin = card_number[:6]
    
    try:
        resp = await safone.bininfo(bin)
        await aux.edit(f"""
<b>Valid Card ✅</b>
<b>┏━◆</b>
<b>┣〖🏦 Bank</b> ⇾<tt>{resp.bank}</tt></b>
<b>┣〖💳 BIN</b> ⇾<tt>{resp.bin}</tt></b>
<b>┣〖🏡 Country</b> ⇾<tt>{resp.country}</tt></b>
<b>┣〖🇮🇳 Flag</b> ⇾<tt>{resp.flag}</tt></b>
<b>┣〖🧿 ISO</b> ⇾<tt>{resp.iso}</tt></b>
<b>┣〖⏳ Level</b> ⇾<tt>{resp.level}</tt></b>
<b>┣〖🔴 Prepaid</b> ⇾<tt>{resp.prepaid}</tt></b>
<b>┣〖🆔 Type</b> ⇾<tt>{resp.type}</tt></b>
<b>┣〖ℹ️ Vendor</b> ⇾<tt>{resp.vendor}</tt></b>
<b>┗━━━◆</b>
""")
    except Exception as e:
        print(f"Error fetching BIN info: {e}")
        return await aux.edit("**🚫 Card not recognized. Please enter a valid card number.**")

