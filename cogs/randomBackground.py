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


def setup(bot):
    bot.add_cog(RandomBackground(bot))