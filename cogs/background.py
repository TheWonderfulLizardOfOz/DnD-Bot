import os.path
from discord.ext import commands
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
        self.cursor.execute(self.personalityStatement)
        results = self.cursor.fetchall()
        self.personality = random.choice(results)[0]
        self.closeDB()

    def setIdeal(self):
        self.openDB()
        self.cursor.execute(self.idealStatement)
        results = self.cursor.fetchall()
        self.ideal = random.choice(results)[0]
        self.closeDB()

    def setBond(self):
        self.openDB()
        self.cursor.execute(self.bondStatement)
        results = self.cursor.fetchall()
        self.bond = random.choice(results)[0]
        self.closeDB()

    def setFlaw(self):
        self.openDB()
        self.cursor.execute(self.flawStatement)
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
        self.setStatements()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        message = self.message()
        await ctx.send(message)

    def setStatements(self):
        self.personalityStatement = """SELECT personalityTrait.personalityTrait 
                FROM PersonalityTrait WHERE personalityTrait.backgroundID = """ + str(self.backgroundID)
        self.idealStatement = """SELECT ideal.ideal FROM ideal WHERE ideal.backgroundID = """ + str(self.backgroundID)
        self.bondStatement = """SELECT bond.bond FROM bond WHERE bond.backgroundID = """ + str(self.backgroundID)
        self.flawStatement = """SELECT flaw.flaw FROM flaw WHERE flaw.backgroundID = """ + str(self.backgroundID)

def setup(bot):
    bot.add_cog(CreateBackground(bot))