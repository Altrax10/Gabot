import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import musik
import valo
from datetime import datetime
import echo
import gi
import pagi
#import chat
import status  
import afk
#import genshing

TOKEN = "NzQ5OTYzMTkxNTg4NDg3MjQ4.GVNSaf.SIA6heSx2u5W7TBPeo3hjSZgn5tZOl-TP8QQwo"
#clientku = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

#for i in range(len(cogs)):
#  cogs[i].setup(client)

class myclient(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
  async def on_ready(self):
    await tree.sync(guild = discord.Object(id=526100423250149386))
    print("moshi moshi")
  
client = myclient(intents = discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.context_menu(name= "klaim", guild = discord.Object(id=526100423250149386))
async def klaim(interaction : discord.Interaction, message : discord.Message):
  await interaction.response.send_message("TerKlaim")
  

client.run(TOKEN)
