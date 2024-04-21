import discord
from discord.ext import commands
import asyncio
import os
import youtube_dl

class Youtube(commands.Cog):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',
        'source_address': '0.0.0.0',
    }

    # FFMPEG_OPTIONS = {
    #     'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    #     'options': '-vn',
    # }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, bot):
        self.bot = bot 
        # super().__init__(source, volume)

        # self.requester = ctx.author
        # self.channel = ctx.channel
        # self.data = data

        # self.uploader = data.get('uploader')
        # self.uploader_url = data.get('uploader_url')
        # date = data.get('upload_date')
        # self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        # self.title = data.get('title')
        # self.thumbnail = data.get('thumbnail')
        # self.description = data.get('description')
        # self.duration = self.parse_duration(int(data.get('duration')))
        # self.tags = data.get('tags')
        # self.url = data.get('webpage_url')
        # self.views = data.get('view_count')
        # self.likes = data.get('like_count')
        # self.dislikes = data.get('dislike_count')
        # self.stream_url = data.get('url')

    # @discord.command()
    # @discord.slash_command(name='play',description='play music')
    # async def play(self,ctx,url):
    #     # Check if the command was issued in a voice channel
    #     if ctx.author.voice is None or ctx.author.voice.channel is None:
    #         await ctx.send("You need to be in a voice channel to use this command!")
    #         return

    #     # Get the voice channel of the user who issued the command
    #     voice_channel = ctx.author.voice.channel
    #     voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    #     await ctx.respond("playing song")

    #     try:
    #         # Connect to the voice channel        
    #         if not voice_client:
    #             voice_client = await voice_channel.connect()
    #         if ctx.voice_client is not None:
    #             await ctx.voice_client.move_to(voice_channel) 
    #         info = self.ytdl.extract_info(url,download=True)

    #         for song in info:
    #             voice_client.play(discord.FFmpegPCMAudio(song,executable="ffmpeg"))


    #     except Exception as e:
    #         print(e)
    #         # await ctx.send("Error connecting to voice channel!")

def setup(bot): 
    bot.add_cog(Youtube(bot)) 