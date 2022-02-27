import discord
from discord.ext import commands

class afk(commands.Cog):
  def __init__ (self, client):
    self.client = client
    
  @commands.command()
  async def afk(self,ctx):
    nama = ctx.message.author.display_name
    await ctx.author.edit(nick=f'[AFK] {nama}')
    await ctx.send(f'{ctx.author.mention} Sekarang AFK')

  @commands.Cog.listener()
  async def on_message(self,message):
    channel = self.client.get_channel(message.channel.id) 
    try:
      if "[AFK]" in message.author.nick:
        await message.author.edit(nick=message.author.nick[5:])
        await channel.send(f"{message.author.mention} Dh Balek")
    except:
      return


def setup(client):
  client.add_cog(afk(client))