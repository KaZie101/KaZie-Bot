import discord
from discord.ext import commands
import asyncio
import os
import random
from pathlib import Path

coughs_dir = 'cogs\\jeff_sounds\\coughs\\'
bowl_tap_dir = 'cogs\\jeff_sounds\\bowl_tap\\'
inhales_dir = 'cogs\\jeff_sounds\\inhales\\'
exhales_dir = 'cogs\\jeff_sounds\\exhales\\'
greetings_dir = 'cogs\\jeff_sounds\\greetings\\'
bong_rip_dir = 'cogs\\jeff_sounds\\bong_rip\\'
random_dir = 'cogs\\jeff_sounds\\random\\'
voice_client = None

class Jeff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot  

    @discord.command()
    @discord.slash_command(name='jeff_smoke',description='Smoke with Jeff')
    async def smoke(self,ctx):
        cough_amount = random.randrange(2,6)
        # Check if the command was issued in a voice channel
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.send("You need to be in a voice channel to use this command!")
            return

        # Get the voice channel of the user who issued the command
        voice_channel = ctx.author.voice.channel
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        await ctx.respond("Drug Party?")

        try:
            # Connect to the voice channel        
            if not voice_client:
                voice_client = await voice_channel.connect()
            if ctx.voice_client is not None:
                await ctx.voice_client.move_to(voice_channel)   

            greeting = os.path.join(greetings_dir,random.choice(os.listdir(greetings_dir)))
            voice_client.play(discord.FFmpegPCMAudio(greeting,executable="ffmpeg"))
            while voice_client.is_playing():
                await asyncio.sleep(1)

            await asyncio.sleep(3)

            bowl_tap = os.path.join(bowl_tap_dir,random.choice(os.listdir(bowl_tap_dir)))
            voice_client.play(discord.FFmpegPCMAudio(bowl_tap,executable="ffmpeg"))
            while voice_client.is_playing():
                await asyncio.sleep(1)

            await asyncio.sleep(2)

            # await asyncio.sleep(random.randrange(2,6))
            bong_rip = os.path.join(bong_rip_dir,random.choice(os.listdir(bong_rip_dir)))
            voice_client.play(discord.FFmpegPCMAudio(bong_rip,executable="ffmpeg"))
            while voice_client.is_playing():
                await asyncio.sleep(1)

            await asyncio.sleep(random.randrange(2,6))

            exhale = os.path.join(exhales_dir,random.choice(os.listdir(exhales_dir)))
            voice_client.play(discord.FFmpegPCMAudio(exhale,executable="ffmpeg"))
            while voice_client.is_playing():
                await asyncio.sleep(1)

            await asyncio.sleep(random.randrange(1,4))

            for coughs in range(cough_amount):
                cough = os.path.join(coughs_dir,random.choice(os.listdir(coughs_dir)))
                voice_client.play(discord.FFmpegPCMAudio(cough,executable="ffmpeg"))
                while voice_client.is_playing():
                    await asyncio.sleep(1)
                await asyncio.sleep(random.randrange(1,2))

            print('Done coughing.')

        except Exception as e:
            print(e)
            # await ctx.send("Error connecting to voice channel!")
            
    @discord.command()
    @discord.slash_command(name='jeff_chicken',description='Whats jeff eating?')
    async def chicken(self,ctx):
        # Check if the command was issued in a voice channel
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.send("You need to be in a voice channel to use this command!")
            return

        # Get the voice channel of the user who issued the command
        voice_channel = ctx.author.voice.channel
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        await ctx.respond("Gas Station Fried Chicken")

        try:
            # Connect to the voice channel        
            if not voice_client:
                voice_client = await voice_channel.connect()
            if ctx.voice_client is not None:
                await ctx.voice_client.move_to(voice_channel)   

            chicken = os.path.join(random_dir,'Jeff - gas station fried chicken.wav')
            voice_client.play(discord.FFmpegPCMAudio(chicken,executable="ffmpeg"))
            while voice_client.is_playing():
                await asyncio.sleep(1)

        except Exception as e:
            print(e)
            # await ctx.send("Error connecting to voice channel!")

def setup(bot): 
    bot.add_cog(Jeff(bot)) 