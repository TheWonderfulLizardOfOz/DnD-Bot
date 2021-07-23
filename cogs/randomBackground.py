from discord.ext import commands
from cogs.background import Background
import random

class RandomBackground(Background):
    def __init__(self, bot):
        super().__init__(bot)
        self.personalityStatement = """SELECT personalityTrait.personalityTrait 
                        FROM PersonalityTrait"""
        self.idealStatement = """SELECT ideal.ideal FROM ideal"""
        self.bondStatement = """SELECT bond.bond FROM bond"""
        self.flawStatement = """SELECT flaw.flaw FROM flaw"""

    @commands.command()
    async def randomBackground(self, ctx):
        self.setBackgroundID()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        self.noLanguages = random.randint(0, 3)
        languages = self.setLanguages()
        self.setLanguageMessage(languages)
        message = self.message()
        await ctx.send(message)

def setup(bot):
    bot.add_cog(RandomBackground(bot))