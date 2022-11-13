import discord
from discord import app_commands
from discord.ext import commands
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
import asyncio 
import os

cogs=[status,musik,valo,echo,gi,pagi,afk]

TOKEN = "NzQ5OTYzMTkxNTg4NDg3MjQ4.GVNSaf.SIA6heSx2u5W7TBPeo3hjSZgn5tZOl-TP8QQwo"
client = commands.Bot(command_prefix = '$', intents = discord.Intents.all(), application_id=749963191588487248)

async def setup_hook(self):
    await self.load_extension(f'echo')
    await tree.synced(guild=discord.object(id=526100423250149386))
            
async def main():
    async with client:
        await client.start(TOKEN)

@client.event
async def on_ready():
  print("moshi moshi")


@client.event
async def on_member_join(member):
  guild = client.get_guild(526100423250149386)
  apatar = member.avatar_url
  uid = member.id
  auth = member.guild.name
  guildav = member.guild.icon_url
  membercount = guild.member_count
  isit = member.bot
  test = member.created_at.strftime("%j")
  test1 = datetime.now()
  test2 = test1.strftime("%j")
  d0 = int(test)
  d1 = int(test2)
  delta = d0 - d1
  member = member.mention
  channel = client.get_channel(751053851456700557)
  sendmsg = channel.send
  embed = discord.Embed(
    title = "Member Joined",
    description = f"User : {member}\n User ID : `({uid})`\n Bot : `{isit}`\n Akun Dibuat : `{delta} Hari yang lalu`",
    colour = discord.Colour.green(),
  )
  embed.set_author(name = auth, icon_url = guildav)
  embed.set_thumbnail(url = apatar)
  embed.set_footer(text = f"{membercount} Members")
  await sendmsg(embed=embed)

@client.event
async def on_member_remove(member):
  guild = client.get_guild(526100423250149386)
  apatar = member.avatar_url
  uid = member.id
  auth = member.guild.name
  guildav = member.guild.icon_url
  membercount = guild.member_count
  test = member.created_at.strftime("%j")
  test1 = datetime.now()
  test2 = test1.strftime("%j")
  d0 = int(test)
  d1 = int(test2)
  delta = d0 - d1
  isit = member.bot
  member = member.mention
  channel = client.get_channel(751053851456700557)
  sendmsg = channel.send
  embed = discord.Embed(
    title = "Member Left",
    description = f"User : {member}\n User ID : `({uid})`\n Bot : `{isit}`\n Akun Dibuat : `{delta} Hari yang lalu`",
    colour = discord.Colour.red()

  )
  embed.set_author(name = auth, icon_url = guildav)
  embed.set_thumbnail(url = apatar)
  embed.set_footer(text = f"{membercount} Members")
  await sendmsg(embed=embed)

@client.event
async def on_message_delete(message):
    channel = client.get_channel(922660132507238431)
    auth = message.author
    guildav = auth.avatar_url
    sendmsg = channel.send
    mem = auth.bot
    if mem == True:
      return
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
    if mem == True:
      return
    else:
      embed = discord.Embed(
        title = "Message Edited",    
        description = f"Sebelum : {message_before.content} \n Sesudah : {message_after.content}",
        colour = discord.Colour.green()
      )
      embed.set_author(name = auth, icon_url = guildav)
      embed.set_footer(text = f'#{message_before.channel}')
      await sendmsg(embed=embed)

@client.command()
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
   


asyncio.run(main())
