import discord
from discord.ext import commands
from _ast import Await
from discord.channel import VoiceChannel
from discord.guild import Guild
from discord.member import Member
import random
from asyncio.tasks import wait
import time
from idlelib.rpc import response_queue
from discord.ext.commands import Bot
import asyncio
import youtube_dl
import os

client = commands.Bot(command_prefix = '.')

url="https://www.youtube.com/watch?v=cScEuPr2C4c"

token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    print("Bot is ready")
        
@client.command()
async def muie(ctx,user:discord.User):
    randomnumber = random.randint(1, 5)
    mention = user.mention
    if(randomnumber == 1):
        response = f"Sa ma pis la {mention} in cap!"
    elif(randomnumber == 2):
        response = f"{mention} sa te ia dracu de picioare!"
    elif(randomnumber == 3):
        response = f"Sa-l vad pe {mention} dansand cu gainile in cociaba lu Olcean!"
    elif(randomnumber == 4):
        response = f"{mention} te tai cu ciorapi cum tai porcu de Craciun!"
    elif(randomnumber == 5):
        response = f"{mention} sa te violeze albastri cum violez eu paiele!"
    elif(randomnumber == 6):
        respons = f"{mention} ba pizzzda unde-i margarinaa?"
    await ctx.send(response)
    await ctx.message.delete()
    
@client.command()
async def supertag(ctx,user:discord.User):
    mention = user.mention
    response = f"Jo {mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention}{mention} te suna politia!"

        
    await ctx.send(response)
    await ctx.message.delete()
    
@client.command()
async def infinit(ctx):
    while (True):
        await ctx.send("Muie!")
    await ctx.message.delete()
        
@client.command()
async def dm(ctx,user:discord.User):
    await user.send("De te vad maine pe strada te sparg")
    await user.send("Mars din fata mea")
    await ctx.message.delete()
  
@client.command()        
async def msg(ctx,user:discord.User,str):
    await user.send(str)
    await ctx.message.delete()
    
@client.command()
async def write(ctx,str):
    await ctx.send(str)
    await ctx.message.delete()
    
@client.command()
async def alarma(ctx):
    
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        
        
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    #player = connected.create_ffmpeg_player('vuvuzela.mp4', after=lambda: print('done'))
    #player.start()
    time.sleep(5)
    await client.voice_clients[0].disconnect()
    

@client.event
async def on_message(message:discord.Message):
    if(message.author.id != client.user.id and "?" in message.content):
        time.sleep(3)
        await message.channel.send("mi-l sugi?")
    await client.process_commands(message)
 
@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel
    
    if before.channel != after.channel and channel.name == "Cantina":
        await member.send("Grija la cantina baiatu! Daca nu mananci nu ai ce cauta aici! Fii atent la albastri cand pleci")
    
    
    
client.run(token)

