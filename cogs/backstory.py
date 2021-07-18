import os.path
import discord
from discord.ext import tasks, commands
import sqlite3
import random

class Backstory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createBackstory(self, ctx):
        self.setBackstoryID()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        message = self.message()
        await ctx.send(message)

    def setBackstoryID(self):
        self.openDB()
        self.cursor.execute("""SELECT backstory.backstoryID, backstory.backstoryName FROM backstory""")
        results = self.cursor.fetchall()
        print(results)
        self.backstoryID = random.choice(results)[0]
        print(self.backstoryID)
        self.backstory = results[self.backstoryID - 1][1]
        print(self.backstory)
        self.closeDB()

    def setPersonality(self):
        self.openDB()
        self.cursor.execute("""SELECT personalityTrait.personalityTrait 
        FROM PersonalityTrait WHERE personalityTrait.backstoryID = ?""", [self.backstoryID])
        results = self.cursor.fetchall()
        self.personality = random.choice(results)[0]
        self.closeDB()

    def setIdeal(self):
        self.openDB()
        self.cursor.execute("""SELECT ideal.ideal FROM ideal WHERE ideal.backstoryID = ?""", [self.backstoryID])
        results = self.cursor.fetchall()
        self.ideal = random.choice(results)[0]
        self.closeDB()

    def setBond(self):
        self.openDB()
        self.cursor.execute("""SELECT bond.bond FROM bond WHERE bond.backstoryID = ?""", [self.backstoryID])
        results = self.cursor.fetchall()
        self.bond = random.choice(results)[0]
        self.closeDB()

    def setFlaw(self):
        self.openDB()
        self.cursor.execute("""SELECT flaw.flaw FROM flaw WHERE flaw.backstoryID = ?""", [self.backstoryID])
        results = self.cursor.fetchall()
        self.flaw = random.choice(results)[0]
        self.closeDB()

    def openDB(self):
        self.db = sqlite3.connect(os.path.dirname(__file__) + '/../backstories.db')
        self.cursor = self.db.cursor()

    def closeDB(self):
        self.db.commit()
        self.db.close()

    def message(self):
        message = """**`Backstory:`** {}
**`Personality Trait:`** {}
**`Ideal:`** {}
**`Bond:`** {}
**`Flaw:`** {}""".format(self.backstory, self.personality, self.ideal, self.bond, self.flaw)
        return message

def setup(bot):
    bot.add_cog(Backstory(bot))