from discord.ext import commands
import random

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def splitArg(self, arg):
        args = arg.split("d")
        for arg in args:
            if arg.isdigit() == False:
                return None
        if len(args) == 2:
            repeats = int(args[0])
            dice = int(args[1])
        elif len(args) == 1:
            repeats = 1
            dice = int(args[0])
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

class RollDice(Roll):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def roll(self, ctx, arg=None):
        if arg == None:
            await ctx.send("Rolling d20...\n" + str(random.randint(1, 20)))
        else:
            nums = self.splitArg(arg)
            if nums == None:
                await ctx.send("Please enter the command as '[number of times rolled]d[dice to roll]'")
            message = self.messageCreator(nums, arg)
            await ctx.send(message)

def setup(bot):
    bot.add_cog(RollDice(bot))