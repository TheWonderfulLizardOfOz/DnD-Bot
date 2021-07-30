import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
load_dotenv(".env")
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!')

extentions = ["cogs.background", "cogs.owner", "cogs.randomBackground", "cogs.dice", "cogs.rollStats",
              "cogs.createCharacter"]

@bot.event
async def on_ready():
    print("bot is ready for stuff")

if __name__ == "__main__":
    for extension in extentions:
        bot.load_extension(extension)

bot.run(TOKEN)
