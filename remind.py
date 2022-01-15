import os
import discord, time, asyncio
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = "/")

@client.command()
async def setrem(ctx, message, minutes):
  await ctx.send('Setting reminder "{}" in {} minutes'.format(message, minutes))
  await asyncio.sleep(60)
  await ctx.send('Reminder: ', message)

@client.command()
async def test(ctx):
  await ctx.send('tester')

client.run(os.getenv('TOKEN'))

print('hello')