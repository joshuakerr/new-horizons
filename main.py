import os
from discord.ext import commands

# logging
import logging
logging.basicConfig(level=logging.INFO)

# flask server
from pseudo_server import keep_alive

# handlers
from core.core_commands import *


bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    # just print initialization info
    #GUILD = os.environ.get("DISCORD_GUILD")
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


# command handlers
bot.add_command(ping)
bot.add_command(check_admin)
bot.add_command(marco)
bot.add_command(sonic)


keep_alive()    # runs a flask server to keep repl.it up
TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
