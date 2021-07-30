from discord.ext import commands
from cogs.background import *
from cogs.dice import *

class CreateCharacter(Background, Roll):
    def __init__(self, bot):
        super().__init__(bot)

    @commands.command()
    async def createCharacter(self, ctx):
        self.setBackgroundID()
        self.setStatements()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        self.getLanguagesNo()
        languages = self.setLanguages()
        self.setLanguageMessage(languages)
        self.setName()
        backMessage = self.message()

        nums = self.rollDice(6, 20)
        statMessage = self.messageCreator(nums)

        await ctx.send(backMessage + "\n" + statMessage)

    def messageCreator(self, nums):
        message = ""
        stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        for i in range(len(stats)):
            message += "**`" + stats[i] + ":`** " + str(nums[i]) +"\n"
        return message

def setup(bot):
    bot.add_cog(CreateCharacter(bot))