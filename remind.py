import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = "/")

@client.command()
async def setrem(ctx, arg1, arg2):
  await ctx.send('reminder set')
  await ctx.send(arg1)


client.run(os.getenv('TOKEN'))

print('hello')