# DnD-Bot

A dnd bot for character creation, currently can only generate a random background.

Requires Discord.py library, and SQL software to edit database directly.

# Extensions:

**cogs.owner** - Extension contains commands that can only be executed by server owner

**cogs.background** - Extension allows for creation of a character's background

**cogs.randomBackground** - Extension allows for creation of a character's background using features from all backgrounds

**cogs.dice** - Extension that rolls dice for the user

**cogs.rollStats** - Extension for rolling stats

# Commands:

**!createBackstory** - Creates a randomly generated background using DnD 5e basic rules backgrounds (so far - will add more when main features are done, only basic rules for now to test features)

**!randomBackstory** - Creates a randomly generated background from different backgrouns using DnD 5e basic rule, a bit more fun but backgrounds might be inconsistent

**!roll** - rolls a d20

**!roll [integer]** rolls a number from 1 to [integer]

**!roll [repeats]d[integer]** - rolls a number from 1 to [integer] and then repeated [repeats] times, each individual roll is output and a total is given

**!rollStatsd20** - rolls stats using a d20

**!load [extension_name]** - Loads an extension, can only be executed by server owner

**!unload [extension_name]** - Unloads an extension, can only be executed by server owner (main use is for removing an extention the server may not want)

**!reload [extension_name]** - Reloads an extension, can only be executed by server owner (main use is to update an extension when the code in extension has been changed whilst main.py is running)

# TODO list

- Members being able to add their own custom backstories and features as well as adding to pre-existing ones
- Add more to background features such as languages, stats and proficiencies
- Different types of stat rolling (e.g 4d6 drop lowest, 4d6, 3d6 etc...)
- Create entire random characters with names, stats and backgrounds
- Other stuff I haven't thought of yet