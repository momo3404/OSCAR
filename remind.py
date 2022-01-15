import os
import discord, time, asyncio, datetime
from datetime import datetime
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

@client.command()
async def setalarm(ctx, message, times):
  await ctx.send('Setting reminder "{}" to alert at {}'.format(message, times))
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
   
  if current_time == times:
    await ctx.send('{} Reminder: {}'.format(ctx.message.author.mention, message))


client.run(os.getenv('TOKEN'))

print('hello')