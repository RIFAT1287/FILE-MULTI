# File-Sharing-Man

Telegram Bot to save Posts or Files that can be Accessed via Special Links.
I Think This Will Be Useful For Many People.

## ⚠️ Disclaimer


I am not responsible for any misuse of this bot.
This bot is intended to help to save desired files which can be accessed via Special Links.
Use these bots at your own risk, and use them wisely.
### Features
- Fully customizable.
- Can be deployed on heroku & vps.
- Customizable welcome message & Forcesub.
- More than one post in one link (batch).
- Flexible FSUB Button can be 1 button or 2 buttons according to the var being filled.

### Setup

- Add bot to Channel Database with all admin permissions
- Add bot to Channel ForceSub add bot as ADMIN
- Add bot to Group ForceSub add bot as ADMIN

## 🛡 Installation
### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://risman.vercel.app/file-deploy.html)</br>

Watch This Tutorial Video on YouTube for Help installing on Heroku<br>
<a href="https://youtu.be/O2tieQgzYZg">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

<details>
<summary><h3><b>🔗 Extra Custom & List Vars</b></h3></summary>

### Variables

* API_HASH Get the HASH API on the web my.telegram.org.
* API_ID Get APP ID on the web my.telegram.org
* TG_BOT_TOKEN Get it from t.me/BotFather
* OWNER Enter Telegram Username for BOT Owner
* CHANNEL_ID Enter the Channel ID for [Channel Database] example:- -100xxxxxxxx
* ADMINS Enter User ID to get Admin rights in BOT
* Optional START_MESSAGE: The /start message initiates a prefix to the bot, Use <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#start_message'>format</a> HTML parsemode
* FORCE_SUB_MESSAGE Optional: Force Subscribe bot message, Use HTML parsemode format
* FORCE_SUB_CHANNEL Enter the ID of the channel for mandatory subscription
* FORCE_SUB_GROUP Enter the ID of the Group for Mandatory Subscription

### Extra Variables

* CUSTOM_CAPTION put your Custom text text if you want to Set Custom Text you can use HTML and <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption' >fillings</a> for formatting (only for documents)
* DISABLE_CHANNEL_BUTTON Enter True to Disable Channel Sharing Button, Default if False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* {first} - User first name
* {last} - User last name
* {id} - User ID
* {mention} - Mention the user
* {username} - Username

#### CUSTOM_CAPTION

* {filename} - file name of the Document
* {previouscaption} - Original Caption

</details>

## 🏷 Support
- Follow Channel [@Lunatic0de](https://t.me/Lunatic0de) for bot update info
- Join Group [@SharingUserbot](https://t.me/SharingUserbot) for discussion, bug reporting and help about File-Sharing-Man.

## 👨🏻‍💻 Credits

- [And](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Risman](https://github.com/mrismanaziz) for [File-Sharing-Man](https://github.com/mrismanaziz/File-Sharing-Man)
- Based on [CodeXBotz](https://github.com/CodeXBotz) Repo [File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot)

## 📑 License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)

[FILE-SHARING-BOT](https://github.com/mrismanaziz/File-Sharing-Man/) is Free Software: You can use, study share and improve it at your
will. specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

##

   Give this Repo a Star if you like it ⭐⭐⭐⭐⭐
