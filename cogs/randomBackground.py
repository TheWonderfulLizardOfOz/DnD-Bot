from discord.ext import commands
from cogs.background import Background


class RandomBackground(Background):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomBackground(self, ctx):
        self.setBackgroundID()
        self.setStatements()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        message = self.message()
        await ctx.send(message)

    def setStatements(self):
        self.personalityStatement = """SELECT personalityTrait.personalityTrait 
                FROM PersonalityTrait"""
        self.idealStatement = """SELECT ideal.ideal FROM ideal"""
        self.bondStatement = """SELECT bond.bond FROM bond"""
        self.flawStatement = """SELECT flaw.flaw FROM flaw"""

    def message(self):
        message = """**`Background:`** {}
**`Personality Trait:`** {}
**`Ideal:`** {}
**`Bond:`** {}
**`Flaw:`** {}""".format(self.background, self.personality, self.ideal, self.bond, self.flaw)
        return message

def setup(bot):
    bot.add_cog(RandomBackground(bot))