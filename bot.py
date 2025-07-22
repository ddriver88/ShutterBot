import os
import random
import base64
import requests
import discord
from discord import app_commands

TOKEN = os.getenv('DISCORD_TOKEN')
CLIENT_ID = os.getenv('SHUTTERSTOCK_CLIENT_ID')
CLIENT_SECRET = os.getenv('SHUTTERSTOCK_CLIENT_SECRET')

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

API_BASE = 'https://api.shutterstock.com/v2/images/search'

@tree.command(name='shutterbot', description='Search Shutterstock for an image')
@app_commands.describe(query='Search keywords')
async def shutterbot(interaction: discord.Interaction, query: str):
    await interaction.response.defer()
    image_url = fetch_random_image(query)
    if image_url:
        await interaction.followup.send(image_url)
    else:
        await interaction.followup.send('No image found.')

def fetch_random_image(query: str) -> str | None:
    if not CLIENT_ID or not CLIENT_SECRET:
        return None
    auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}"}
    params = {
        "query": query,
        "per_page": 50,
        "image_type": "photo"
    }
    resp = requests.get(API_BASE, headers=headers, params=params)
    if resp.status_code != 200:
        return None
    data = resp.json()
    hits = data.get('data', [])
    if not hits:
        return None
    image = random.choice(hits)
    return image.get('assets', {}).get('preview', {}).get('url')

@bot.event
async def on_ready():
    await tree.sync()
    print(f'Logged in as {bot.user}')

if __name__ == '__main__':
    if not TOKEN:
        raise SystemExit('DISCORD_TOKEN not set')
    bot.run(TOKEN)
