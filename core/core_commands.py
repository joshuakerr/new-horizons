# core_commands.py
# basic commands

from discord.ext import commands


@commands.command(name='ping', help='Checks bot status.')
async def ping(ctx):
    await ctx.send('PONG!')


@commands.command(name='admin', help='Shows admin status.')
@commands.has_role('admin')
async def check_admin(ctx, channel_name='test-channel'):
    await ctx.send('All hail the mighty administrator!')


@commands.command(name='marco', help='Checks bot status.')
async def marco(ctx):
    await ctx.send('Polo!')


@commands.command(name='sonic', help='Checks bot status.')
async def sonic(ctx):
    await ctx.send('Speed!')
    