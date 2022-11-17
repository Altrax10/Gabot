import discord
from discord import app_commands
from discord.ext import commands

class slash(commands.Cog):
  def __init__ (self, bot: commands.Bot ):
    self.bot = bot
    
  @app_commands.command(name="sync")
  async def sync(self, interaction: discord.Interaction) -> None:
    client = self.bot
    await client.tree.sync()
    await interaction.response.send_message("Synced")
   
async def setup(bot):
    await bot.add_cog(slash(bot))
