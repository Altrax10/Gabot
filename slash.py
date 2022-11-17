import discord
from discord import app_commands
from discord.ext import commands

class slash(commands.Cog):
  def __init__ (self, bot: commands.Bot ):
    self.bot = bot
    
  @app_commands.command(name="command-1")
  async def my_command(self, interaction: discord.Interaction) -> None:
    """ /command-1 """
    await interaction.response.send_message("Hello from command 1!", ephemeral=True)
   
async def setup(bot):
    await bot.add_cog(slash(bot))
