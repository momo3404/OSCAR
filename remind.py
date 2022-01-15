import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = "/")

@client.command()
async def setrem(ctx, message):
  if message == 'set reminder':
    await ctx.send('reminder set')


client.run(os.getenv('TOKEN'))

print('hello')