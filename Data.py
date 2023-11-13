# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for This Bot
 ├ /start - Start Bot
 ├ /about - About this Bot
 ├ /help - Help this Bot Command
 ├ /ping - To check live bots
 └ /uptime - To view bot status
👨‍💻 Develoved by </b><a href='https://t.me/TheAnimeLoungeOwner'>@TheAnimeLoungeOwner</a>
"""

    close = [
        [InlineKeyboardButton("CLOSE", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ABOUT", callback_data="about"),
            InlineKeyboardButton("CLOSE", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About this Bot:

@{} is a Telegram Bot for saving Posts or Files that can be Accessed via a Special Link.

 • Creator: @TheAnimeLoungeOwner
👨‍💻 Develoved by </b><a href='https://t.me/TheAnimeLoungeOwner'>@TheAnimeLounge</a>
"""
