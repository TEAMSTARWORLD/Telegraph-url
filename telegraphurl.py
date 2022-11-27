#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MediaToTelegraphLink bot by STAR WORLD] (https://github.com/TEAMSTARWORLD/Telegraph-url)

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

startips=Client(
    "Telegraph-url",
    api_id = int(os.environ['API_ID']),
    api_hash = os.environ['API_HASH'],
    bot_token = os.environ['BOT_TOKEN']
)

@startips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
Heya {message.from_user.mention},
ɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋs ғᴏʀ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ғɪʟᴇs.

sɪᴍᴘʟʏ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ ғɪʟᴇ ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ᴛʜɪs ᴄʜᴀᴛ.

ᴠᴀʟɪᴅ ғɪʟᴇ ᴛʏᴘᴇs ᴀʀᴇ 'ᴊᴘᴇɢ', 'ᴊᴘɢ', 'ᴘɴɢ', 'ᴍᴘ𝟺' ᴀɴᴅ 'ɢɪғ'.  

ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟɪɴᴋs ɪɴ **ɢʀᴏᴜᴘ ᴄʜᴀᴛs**, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ sᴜᴘᴇʀɢʀᴏᴜᴘ ᴀɴᴅ sᴇɴᴅ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ <code>/tl</code> ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ ғɪʟᴇ.

Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ :[𝗦𝗧𝝙𝗥𝗪𝗢𝗥𝗟𝗗](https://t.me/TG_STARWORLD) !

𝗦𝗨𝗣𝗣𝗢𝗥𝗧 :[ᴄʟɪᴄᴋ ʜᴇʀᴇ ✨](https://t.me/TEACH_TEAMOP)
            """
    await startips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@startips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
        async def progress(current, total):
            await text.edit_text(f"📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴍᴇᴅɪᴀ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 Uploading to Telegraph...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@startips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")
        async def progress(current, total):
            await text.edit_text(f"📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴍᴇᴅɪᴀ... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           
        
print("STAR Bot is alive!")
startips.run()

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
