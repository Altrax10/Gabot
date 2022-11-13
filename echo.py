import discord
from discord.ext import commands

class echo(commands.Cog):
  def __init__ (self, bot: commands.Bot ):
    self.bot = bot
  @commands.command()
  async def echo(self,ctx):
    client = self.bot
    msg = ctx.message.content
    msg1 = msg[5:]
    idku = ctx.message.channel
    idnya = idku.id
    channel = bot.get_channel(idnya)
    sendmsg = channel.send
    #reaction = ":valosagethumbsup:925975156608880640"
    await ctx.message.delete()
    await ctx.trigger_typing()
    await sendmsg(msg1)
    #await cek.add_reaction(reaction)
async def setup(bot):
    await bot.add_cog(echo(bot))
