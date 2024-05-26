import asyncio
import importlib
from pyrogram import idle
from EQUROBOT import app
from EQUROBOT.modules import ALL_MODULES
import config
from config import LOGGER_ID

LOGGER_ID = config.LOGGER_ID

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("EQUROBOT.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await app.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝖺𝗅𝗂𝗏𝖾 𝖡𝖺𝖻𝗒 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝖣𝖾𝗉𝗅𝗈𝗒 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [‣𝗠𝗥 𝗫 𝗕𝗥𝗢𝗞𝗘𝗡⋆](https://t.me/MRBROKN)**")
    await idle()
    print("𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗫 𝗕𝗥𝗢𝗞𝗘𝗡")
  
  
if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
    
