# Project Description

[text here]


# Code Standards

1. Compartmentalize : make everything as modular as possible
2. Comment : use lots of comments. Use a """comment""" at the top of every function/class


# File Structure

- main.py               launch and initialize the bot
- .env                  stores environment variables (hidden from public code)
- pseudo_server.py      simple flask server to keep app up
        without this, repl.it will think the app is done and will shut it off

- /core                 basic functionality
    handlers.py         command handlers
    core.py             core functions
    admin.py            administrative functions
    decorators.py       decorators
    util.py             simple utility functions
    help.py             functions related to help
    output.py           functions to talk to players

- /resources
    strings.py          miscellaneous strings
    regex.py            miscellaneous regex strings

- /database             database functions
    db.py               initialize database
    items.py            item database functions
    enemies.py          enemies database functions
    quests.py           quest database functions
    characters.py       character database functions

- /enemies              related to enemies

- /items                related to items

- /quests               related to quests

- /characters           related to characters

