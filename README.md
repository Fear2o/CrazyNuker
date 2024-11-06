# 🌌Powerful Discord Nuker Bot 🌌



> ⚠️ **Educational Purposes Only** ⚠️  
> This bot is designed for experimental learning and should **only** be used in environments where you have explicit permission from server owners. Misuse can result in serious consequences like account suspension or legal action. Use responsibly!


![GitHub stars](https://img.shields.io/github/stars/Fear2o/DiscordNuker?style=social)
![Build Status](https://img.shields.io/github/workflow/status/Fear2o/DiscordNuker/CI)
![License](https://img.shields.io/github/license/Fear2o/DiscordNuker)
![Contributors](https://img.shields.io/github/contributors/Fear2o/DiscordNuker)


## ✨ Features
- 🔥 **Server Renaming**: Changes the server name to a custom setting.
- 💣 **Channel Deletion**: Removes all existing text channels in the server.
- 📢 **Mass Channel Creation & Super Quick Spam**: Creates multiple text channels and sends a thousands of messages/pings in a short duration.

## 🚀 Setup Instructions

### 1. Clone the Repository
First, clone this repository to your local machine.  
```bash
git clone https://github.com/Fear2o/DiscordNuker
cd DiscordNuker
```

### 2. Install Dependencies
Ensure you have Python installed (3.8 or higher). Then, install `discord.py` by running:
```bash
pip install -U discord.py
```

### 3. Configure the Bot
Open `bot.py` in a text editor and replace `'your_token_here'` with your **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications).

Customize these variables as desired:
- `GUILD_NAME`: The new name for the server (e.g., `"Fear is everywhere"`).
- `CHANNEL_NAME`: The name for channels to be created (e.g., `"fear has hacked you"`).
- `SPAM_MESSAGE`: The message that will be spammed in each created channel.

### 4. Enable Intents
In the [Discord Developer Portal](https://discord.com/developers/applications), ensure **Message Content Intent** is enabled. This is required for the bot to read and respond to messages effectively.

### 5. Run the Bot
Start the bot by running:
```bash
python bot.py
```

### 6. Trigger the Nuke Command
in a server with the bot added, type the following command to start the nuke operation:
```diff
!nuke
```
This will initiate the bot to rename the server, delete all channels, and create multiple new channels filled with spam messages.

## ⚙️ Important Notes
- **Rate Limits**: To avoid hitting Discord’s rate limits, the bot includes small delays between messages.
- **Permissions**: The bot must have sufficient permissions to manage channels, manage server and send messages in the target server.
- **Legal Disclaimer**: Unauthorized usage of this bot on Discord servers is a violation of [Discord's Terms of Service](https://discord.com/terms) and may lead to account suspension or legal action.

## 🖥️ Supported Platforms
- **Windows**: Fully supported.
- **Linux**: Works with minor adjustments.
- **macOS**: May require additional dependencies for full functionality.


## 🌟 Contributing & Support
Feel free to star ⭐ the repo if you find this project useful! Contributions are welcome to improve functionality and add new features.


## 📜 Disclaimer
This tool is intended for **educational purposes only**. Unauthorized or malicious use is strictly prohibited. Respect Discord’s guidelines and obtain necessary permissions before running this bot in any server environment.

**____________________________________________**


*Crafted with passion by Fear.io*










