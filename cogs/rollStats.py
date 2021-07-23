from cogs.dice import Roll
from discord.ext import commands
import random

class RollStats(Roll):
    def __init__(self, bot):
        super().__init__(bot)
        self.minVal = []
        self.statTotals = []

    @commands.command()
    async def rollStatsd20(self, ctx):
        nums = self.rollDice(6, 20)
        message = self.messageCreator(nums)
        await ctx.send(message)

    @commands.command()
    async def rollStats4d6Drop(self, ctx):
        self.roll4d6()
        self.dropLowest()
        message = self.messageCreator(self.statTotals)
        await ctx.send(message)

    @commands.command()
    async def rollStats4d6(self, ctx):
        self.roll4d6()
        message = self.messageCreator(self.statTotals)
        await ctx.send(message)

    def roll4d6(self):
        self.statTotals = []
        self.minVal = []
        for i in range(6):
            nums = self.rollDice(4, 6)
            self.minVal.append(min(nums))
            self.statTotals.append(sum(nums))

    def dropLowest(self):
        print(self.minVal)
        print(self.statTotals)
        for i in range(len(self.minVal)):
            self.statTotals[i] = self.statTotals[i] - self.minVal[i]

    def messageCreator(self, nums):
        message = ""
        stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for i in range(len(stats)):
            message += "**`" + stats[i] + ":`** " + str(nums[i]) +"\n"
        return message

def setup(bot):
    bot.add_cog(RollStats(bot))