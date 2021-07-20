import os.path
import discord
from discord.ext import tasks, commands
import random

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, arg = None):
        if arg == None:
            await ctx.send("Rolling d20...\n" + str(random.randint(1, 20)))
        nums = self.splitArg(arg)
        print(nums)
        if nums == None:
            await ctx.send("Please enter the command as '[number of times rolled]d[dice to roll]'")
        message = self.messageCreator(nums, arg)
        await ctx.send(message)

    def splitArg(self, arg):
        arg = arg.split("d")
        print(arg)
        if len(arg) == 2:
            repeats = int(arg[0])
            dice = int(arg[1])
        elif arg[0].isdigit() == False:
            return None
        elif len(arg) == 1:
            repeats = 1
            dice = int(arg[0])
        nums = self.rollDice(repeats, dice)
        return nums

    def rollDice(self, repeats, dice):
        nums = []
        for i in range(repeats):
            nums.append(random.randint(1, dice))
        return nums

    def messageCreator(self, nums, arg):
        message = "Rolling " + arg + "..."
        total = 0
        for num in nums:
            result = random.randint(1, num)
            total += result
            message += "\n" + str(result)
        if len(nums) != 1:
            message += "\n = " + str(total)
        return message

def setup(bot):
    bot.add_cog(Roll(bot))