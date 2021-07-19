import os.path
import discord
from discord.ext import tasks, commands
from cogs.background import Background
import sqlite3
import random


class RandomBackground(Background):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomBackground(self, ctx):
        self.setBackgroundID()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        message = self.message()
        await ctx.send(message)

    def setPersonality(self):
        self.openDB()
        self.cursor.execute("""SELECT personalityTrait.personalityTrait 
        FROM PersonalityTrait""")
        results = self.cursor.fetchall()
        self.personality = random.choice(results)[0]
        self.closeDB()

    def setIdeal(self):
        self.openDB()
        self.cursor.execute("""SELECT ideal.ideal FROM ideal""")
        results = self.cursor.fetchall()
        self.ideal = random.choice(results)[0]
        self.closeDB()

    def setBond(self):
        self.openDB()
        self.cursor.execute("""SELECT bond.bond FROM bond""")
        results = self.cursor.fetchall()
        self.bond = random.choice(results)[0]
        self.closeDB()

    def setFlaw(self):
        self.openDB()
        self.cursor.execute("""SELECT flaw.flaw FROM flaw""")
        results = self.cursor.fetchall()
        self.flaw = random.choice(results)[0]
        self.closeDB()


def setup(bot):
    bot.add_cog(RandomBackground(bot))