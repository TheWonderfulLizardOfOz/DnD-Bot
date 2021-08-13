# DnD-Bot

A dnd bot for character creation, currently can only generate a random background.

Requires Discord.py library, and an SQL browser if you want to edit database directly/sqlite3 library to edit using a program.

Backgrounds/Races already added are from basic rules

# Extensions:

**cogs.owner** - Extension contains commands that can only be executed by server owner

**cogs.background** - Extension allows for creation of a character's background

**cogs.randomBackground** - Extension allows for creation of a character's background using features from all backgrounds

**cogs.dice** - Extension that rolls dice for the user

**cogs.rollStats** - Extension for rolling stats

**cogs.createCharacter** - Extension for creating a character

**cogs.addItem** - Extension for adding custom items to names/races/backgrounds etc...

# Commands:

**!createBackstory** - Creates a randomly generated background using DnD 5e basic rules backgrounds (so far - will add more when main features are done, only basic rules for now to test features)

**!randomBackstory** - Creates a randomly generated background from different backgrouns using DnD 5e basic rule, a bit more fun but backgrounds might be full of contradictions

**!roll** - rolls a d20

**!roll [integer]** rolls a number from 1 to [integer]

**!roll [repeats]d[integer]** - rolls a number from 1 to [integer] and then repeated [repeats] times, each individual roll is output and a total is given

**!rollStatsd20** - rolls stats using a d20

**!rollStats4d6Drop** - rolls stats using the 4d6 drop lowest rule

**!rollStats4d6** - rolls stats using a 4d6

**!createCharacter** - Creates a character with stats, backstory, name and race

**!name** - Outputs a randomly selected name from a textfile

**!addName** - Add name to textfile

**!load [extension_name]** - Loads an extension, can only be executed by server owner

**!unload [extension_name]** - Unloads an extension, can only be executed by server owner (main use is for removing an extention the server may not want)

**!reload [extension_name]** - Reloads an extension, can only be executed by server owner (main use is to update an extension when the code in extension has been changed whilst main.py is running)

# TODO list

- Members adding custom races, backstories, names and languages
- Add proficiencies to create background proficiencies
- More types of stat rolling
- Clean up the code because the inheritance is a mess
- Add more backgrounds and races that aren't from basic rules
- Other stuff I haven't thought of yet