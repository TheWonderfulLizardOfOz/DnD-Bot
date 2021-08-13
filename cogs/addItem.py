import os.path
from discord.ext import commands
import sqlite3

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addName(self, ctx, arg = None):
        if arg is not None and arg.isalpha() == True:
            newName = self.checkName(arg)
            if newName == True:
                self.addNameToFile(arg)
                await ctx.send("Name added :)")
            else:
                await ctx.send("Name has already been added")
        else:
            if arg is None:
                await ctx.send("Please format command as !addName [name]")
            else:
                await ctx.send("Please don't include non alphanumeric characters")

    def checkName(self, arg):
        with open(os.path.dirname(__file__) + "/../names.txt", "r") as file:
            for name in file:
                if name.strip(",\n") == arg.title():
                    return False
        return True

    def addNameToFile(self, name):
        with open(os.path.dirname(__file__) + "/../names.txt", "a") as file:
            file.write(str(name).title() + ",\n")

def setup(bot):
    bot.add_cog(Add(bot))