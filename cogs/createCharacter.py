from discord.ext import commands
from cogs.background import *
from cogs.dice import *
import os.path
import json

class CreateCharacter(Background, Roll):
    def __init__(self, bot):
        super().__init__(bot)
        with open(os.path.dirname(__file__) + "/../races.json", "r") as jsonFile:
            self.raceDict = json.load(jsonFile)
        self.race = ""
        self.stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        self.racialTraits = []

    @commands.command()
    async def createCharacter(self, ctx):
        self.setBackgroundID()
        self.setStatements()
        self.setPersonality()
        self.setIdeal()
        self.setBond()
        self.setFlaw()
        self.getLanguagesNo()
        self.roll4d6()
        self.dropLowest()
        self.setRace()
        languages = self.setLanguages()
        self.setLanguageMessage(languages)
        self.setName()
        backMessage = self.message()
        statMessage = self.messageCreator()
        raceMessage = self.createRaceMessage()
        await ctx.send(backMessage + "\n" + statMessage + raceMessage)

    def setRace(self):
        raceList = []
        for race in self.raceDict:
            raceList.append(race)
        self.race = random.choice(raceList)
        raceAttributes = self.raceDict[self.race]
        self.addRandBonus(raceAttributes)
        for i in range(len(self.stats)):
            self.statTotals[i] += raceAttributes.get(self.stats[i], 0)
        self.noLanguages += raceAttributes.get("languages bonus", 0)
        self.setRacialTraits(raceAttributes)

    def addRandBonus(self, raceAttributes):
        randBonus = raceAttributes.get("random bonus")
        if randBonus is not None:
            for i in range(randBonus[0]):
                statToAdd = random.choice(self.stats)
                if raceAttributes.get(statToAdd, 0) == 0:
                    statIndex = self.stats.index(statToAdd)
                    self.statTotals[statIndex] += randBonus[1]

    def setRacialTraits(self, raceAttributes):
        self.racialTraits = []
        for trait in raceAttributes["traits"]:
            self.racialTraits.append(trait)

    def messageCreator(self):
        message = ""
        for i in range(len(self.stats)):
            message += "**`" + self.stats[i].title() + ":`** " + str(self.statTotals[i]) +"\n"
        return message

    def createRaceMessage(self):
        message = "**`Race:`** " + self.race + "\n**`Racial Traits:`** "
        for trait in self.racialTraits:
            message += trait + ", "
        message = message[:-2]
        return message


def setup(bot):
    bot.add_cog(CreateCharacter(bot))