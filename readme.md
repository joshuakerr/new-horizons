# Project Description

[text here]


## Code Standards

1. Compartmentalize : make everything as modular as possible
2. Comment : use lots of comments. Use a """comment""" at the top of every function/class
3. Commit messages : use commit messages to update project

## File Structure

| File             | Description                                            |
|------------------|--------------------------------------------------------|
| main.py          | launch and initialize the bot                          |
| .env             | stores environment variables (hidden from public code) |
| pseudo_server.py | simple flask server to keep app running on repl.it     |
|                  |                                                        |
| **/core**        | basic functionality                                    |
| -- handlers.py   | command handlers                                       |
| -- core.py       | core functions                                         |
| -- admin.py      | administrative functions                               |
| -- decorators.py | decorators                                             |
| -- util.py       | simple utility functions                               |
| -- help.py       | functions related to help                              |
| -- output.py     | functions to talk to players                           |
|                  |                                                        |
| **/resources**   | string and regex resources                             |
| -- strings.py    | basic string resources                                 |
| -- regex.py      | regular expressions                                    |
|                  |                                                        |
| **/database**    | database functions                                     |
| -- db.py         | initialize database                                    |
|                  |                                                        |
| **/enemies**     | related to enemies                                     |
|                  |                                                        |
| **/items**       | related to items                                       |
|                  |                                                        |
| **/quests**      | related to quests                                      |
|                  |                                                        |
| **/characters**  | related to characters                                  |
|                  |                                                        |

(use https://www.tablesgenerator.com/markdown_tables)