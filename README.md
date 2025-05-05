# Nexus Mods Fan-Made Discord Bot
This is a fan made bot written in Python that provides seamless integration with Nexus Mods to fetch and display the latest trending, and popular mods for your favorite games. This bot allows users to interact with the Nexus Mods API to get mod information directly from Discord.

## Features
- **Latest Added Mods**: Display the most recently added mods for any supported game.
- **Updated Mods**: Display most recently updated mods for any supported game.
- **Trending Mods**: Display the top 10 trending mods for any supported game.
- **Browse Games**: Display  all available games on Nexus Mods.
- **Search Game**: Search for a specific game on Nexus Mods.
- **Search Mod**: Search for a specific mod on Nexus Mods.

## Installation
1. Clone the repository
2. Create a `.env` file:
  ```bash
  DISCORD_TOKEN=your_bot_token
  API_KEY="your-api-key"
  API_BASE_URL="https://api.nexusmods.com/"
  ```
3. To get your own API Key, follow these steps:
   1. Register/Login to [Nexus Mods](https://www.nexusmods.com/users/myaccount?tab=api%20access)
   2. Navigate to **Nexus Mod Integration*** under Integrations.
   3. Request API Key.
4. Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
5. Start the bot:
  ```bash
  python main.py
  ```

## Configuration
1. In the project root, create a `.env` file with the following contents:
```bash
DISCORD_TOKEN=your_discord_bot_token
API_KEY=your_nexus_mods_api_key
```