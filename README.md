# ShutterBot

ShutterBot is a simple Discord bot that returns random Shutterstock images based on a search query.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create a Discord application and bot, then copy the bot token.
3. Obtain Shutterstock API credentials (client ID and client secret).
4. Set the following environment variables:
   - `DISCORD_TOKEN`
   - `SHUTTERSTOCK_CLIENT_ID`
   - `SHUTTERSTOCK_CLIENT_SECRET`
5. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

Use the `/shutterbot` slash command followed by your query to get a random photo from Shutterstock.
