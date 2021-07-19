import os.path
import discord
from discord.ext import tasks, commands
import sqlite3
import random

class Background(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def setBackgroundID(self):
        self.openDB()
        self.cursor.execute("""SELECT background.backgroundID, background.backgroundName FROM background""")
        results = self.cursor.fetchall()
        self.backgroundID = random.choice(results)[0]
        self.background = results[self.backgroundID - 1][1]
        self.closeDB()

    def setPersonality(self):
        self.openDB()
        self.cursor.execute("""SELECT personalityTrait.personalityTrait 
        FROM PersonalityTrait WHERE personalityTrait.backgroundID = ?""", [self.backgroundID])
        results = self.cursor.fetchall()
        self.personality = random.choice(results)[0]
        self.closeDB()

    def setIdeal(self):
        self.openDB()
        self.cursor.execute("""SELECT ideal.ideal FROM ideal WHERE ideal.backgroundID = ?""", [self.backgroundID])
        results = self.cursor.fetchall()
        self.ideal = random.choice(results)[0]
        self.closeDB()

    def setBond(self):
        self.openDB()
        self.cursor.execute("""SELECT bond.bond FROM bond WHERE bond.backgroundID = ?""", [self.backgroundID])
        results = self.cursor.fetchall()
        self.bond = random.choice(results)[0]
        self.closeDB()

    def setFlaw(self):
        self.openDB()
        self.cursor.execute("""SELECT flaw.flaw FROM flaw WHERE flaw.backgroundID = ?""", [self.backgroundID])
        results = self.cursor.fetchall()
        self.flaw = random.choice(results)[0]
        self.closeDB()

    def openDB(self):
        self.db = sqlite3.connect(os.path.dirname(__file__) + '/../backgrounds.db')
        self.cursor = self.db.cursor()

    def closeDB(self):
        self.db.commit()
        self.db.close()

    def message(self):
        message = """**`Background:`** {}
**`Personality Trait:`** {}
**`Ideal:`** {}
**`Bond:`** {}
**`Flaw:`** {}""".format(self.background, self.personality, self.ideal, self.bond, self.flaw)
        return message

class CreateBackground(Background):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createBackground(self, ctx):
        self.setBackgroundID()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        message = self.message()
        await ctx.send(message)

def setup(bot):
    bot.add_cog(CreateBackground(bot))