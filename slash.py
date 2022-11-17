import discord
from discord import app_commands
from discord.ext import commands
import speedtest

class slash(commands.Cog):
  def __init__ (self, bot: commands.Bot ):
    self.bot = bot
 
  speed_test = speedtest.Speedtest()

  async def bytes_to_mb(bytes):
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    return int(bytes/MB)

  async def kecepatan():
    
    download_speed = bytes_to_mb(speed_test.download())
    upload_speed = bytes_to_mb(speed_test.upload())

    return download_speed
    return upload_speed

  @app_commands.command(name="ping")
  async def ping(self, interaction: discord.Interaction) -> None:

    #await interaction.response.defer(ephemeral = True)
    #await asyncio.sleep(4)
    #await interaction.followup.send('yo')
    await interaction.response.send_message(f"Download = {download_speed}n/ Upload = {upload_speed}")
   
async def setup(bot):
    await bot.add_cog(slash(bot))

