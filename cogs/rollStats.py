from cogs.dice import Roll
from discord.ext import commands
import random

class RollStats(Roll):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rollStatsd20(self, ctx):
        nums = self.rollDice(6, 20)
        message = self.messageCreator(nums)
        await ctx.send(message)

    def messageCreator(self, nums):
        message = ""
        stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for i in range(len(stats)):
            message += "**`" + stats[i] + ":`** " + str(nums[i]) +"\n"
        return message

def setup(bot):
    bot.add_cog(RollStats(bot))