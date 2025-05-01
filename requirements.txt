# Nexus Mods Fan-Made Discord Bot
Welcome to the **Nexus Mods Discord Bot (Python)**! This is a fan made bot written in Python that provides seamless integration with Nexus Mods to fetch and display the latest, trending, and popular mods for your favorite games. This bot allows users to interact with the Nexus Mods API to get mod information directly from Discord.

## Features
- **Trending Mods**: Fetch the top 10 trending mods for any supported game.
- **Latest Added Mods**: View the most recently added mods for any supported game.
- **Mod Pagination**: Navigate through multiple pages of mods to find what you are looking for.

## Installation
### 1. Clone the repository:
```bash
git clone https://github.com/Khai-08/Nexus-Mods.git
cd nexus-mods-bot
```

### 2. Install dependencies
Make sure to install the required libraries:
```bash
pip install -r requirements.txt
```

### 3. Setup the bot
In the project folder, create a `.env` file with the following contents:
```bash
DISCORD_TOKEN=your_discord_bot_token
API_HEADERS=your_nexus_mods_api_headers
```

### 4. Run the bot
To start the bot, simply run:
```bash
python main.py
```