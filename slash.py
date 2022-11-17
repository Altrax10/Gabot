import discord
from discord import app_commands
from discord.ext import commands
import speedtest

class slash(commands.Cog):
  def __init__ (self, bot: commands.Bot ):
    self.bot = bot

  @app_commands.command(name="ping", description ="Speed Test")
  async def ping(self, interaction: discord.Interaction) -> None:
    speed_test = speedtest.Speedtest()
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    download_speed = speed_test.download()
    upload_speed = speed_test.upload()

    await Interaction.response.defer(ephemeral = True)
    await asyncio.sleep(20)
    await Interaction.followup.send('yo')
    print(download_speed)
    print(upload_speed)
    #await interaction.response.send_message(f"Download = {download_speed}n/ Upload = {upload_speed}")
   
async def setup(bot):
    await bot.add_cog(slash(bot))

