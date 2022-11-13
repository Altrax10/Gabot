import discord
from discord.ext import commands
   
@commands.command()
async def echo(self,ctx):
    client = self.client
    msg = ctx.message.content
    msg1 = msg[5:]
    idku = ctx.message.channel
    idnya = idku.id
    channel = client.get_channel(idnya)
    sendmsg = channel.send
    #reaction = ":valosagethumbsup:925975156608880640"
    await ctx.message.delete()
    await ctx.trigger_typing()
    await sendmsg(msg1)
    #await cek.add_reaction(reaction)

async def setup(bot):
    await bot.add_cog(echo(bot))
