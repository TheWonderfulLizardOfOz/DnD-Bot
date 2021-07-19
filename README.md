# DnD-Bot

A dnd bot for character creation, currently can only generate a random background.

Requires Discord.py library, and SQL software to edit database directly.

# Extensions:

**cogs.owner** - Extension contains commands that can only be executed by server owner

**cogs.background** - Extension allows for creation of a character's background

**cogs.randomBackground** - Extension allows for creation of a character's background using features from all backgrounds

# Commands:

**!createBackstory** - Creates a randomly generated background using DnD 5e basic rules backgrounds (so far - will add more when main features are done, only basic rules for now to test features)

**!randomBackstory** - Creates a randomly generated background from different backgrouns using DnD 5e basic rule, a bit more fun but backgrounds might be inconsistent

**!load [extension_name]** - Loads an extension, can only be executed by server owner

**!unload [extension_name]** - Unloads an extension, can only be executed by server owner (main use is for removing an extention the server may not want)

**!reload [extension_name]** - Reloads an extension, can only be executed by server owner (main use is to update an extension when the code in extension has been changed whilst main.py is running)

# TODO list

- Members being able to add their own custom backstories and features as well as adding to pre-existing ones
- Dice roller that could respond tp !roll d4 or !roll 5d7 or any combinations and output a total
- Add more to background features such as languages, stats and proficiencies
- Rolling stats (maybe with an option of usig different stat rolling rules such as d20 or 4d6 etc...)
- Create entire random characters with names, stats and backgrounds
- Other stuff I haven't thought of yet