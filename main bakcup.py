import keep_alive
import os
import discord
from discord.ext import commands
import music
import valo
import gatelogs
import datetime 
import pytz
import tzdata
import echo

cogs=[music,valo,gatelogs,echo]

TOKEN = os.environ['TOKEN']
client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

@client.event
async def on_ready():
    print("moshi moshi")
    while True:
      dtobj1=datetime.datetime.utcnow()
      dtobj3=dtobj1.replace(tzinfo=pytz.UTC)
      dtobj=dtobj3.astimezone(pytz.timezone("Asia/Kuala_Lumpur"))
      jam = dtobj.hour
      if jam >= 17 and jam <= 18:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="💤💤💤"))

      else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="OnePiece"))

@client.event
async def on_message_delete(message):
    channel = client.get_channel(922660132507238431)
    auth = message.author
    guildav = auth.avatar_url
    sendmsg = channel.send
    mem = auth.bot
    if mem == True:
      await sendmsg("This Message Sent By a Bot")
    else:
      embed = discord.Embed(
        title = "Message Deleted",    
        description = message.content,
        colour = discord.Colour.red()
      )
      embed.set_author(name = auth, icon_url = guildav)
      embed.set_footer(text = f'#{message.channel}')
      await sendmsg(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):
    channel = client.get_channel(922660132507238431)
    auth = message_before.author
    mem = auth.bot
    guildav = auth.avatar_url
    sendmsg = channel.send
    print(mem)
    if mem == True:
      await sendmsg("This Message Sent By a Bot")
    else:
      embed = discord.Embed(
        title = "Message Edited",    
        description = f"Sebelum : {message_before.content} \n Sesudah : {message_after.content}",
        colour = discord.Colour.green()
      )
      embed.set_author(name = auth, icon_url = guildav)
      embed.set_footer(text = f'#{message_before.channel}')
      await sendmsg(embed=embed)

keep_alive.keep_alive()
client.run(TOKEN)

