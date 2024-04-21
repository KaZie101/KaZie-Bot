import discord
import os
from dotenv.main import load_dotenv
from pathlib import Path


load_dotenv()
token = str(os.getenv("DISCORD_TOKEN"))
bot = discord.Bot()

voice_client = None
cogs_list = [
    'jeff',
    'youtube'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
    
    
# Event to perform actions when the bot is ready
@bot.listen()
async def on_connect():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.sync_commands(force=True)
# Run the bot with your Discord bot token
bot.run(token)
