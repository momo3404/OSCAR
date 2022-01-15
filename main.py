import os
import discord, json
import time, asyncio
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = "/")


# todo starts here

db = dict()  # or mongodb


client = commands.Bot(command_prefix = "/")



# activate via "/todo ... "
# commands:
#   /todo add [desc] [date time]
#   /todo display   (in n)
#   /tdo  
# -------------------------------
@client.command()
async def todo(ctx, arg1):
    author = ctx.message.author
    print(author)
    if arg1 == "add":
        addToDo(arg1, author)
        await ctx.send("added!")
    elif arg1 == "display":
        await ctx.send("displaying...")
        for item in db[author]:
            await ctx.send(item)
    else:
        await ctx.send("something else")
# ----------------------
# add msg to the db written by author
# 
# ----------------------
def addToDo(msg, author):
    if (author in db.keys()):
        db[author].add(msg)
    else: # case: this is new person
        db[author] = {msg}


def display():
    pass

# todo finishes here

# remind starts here
@client.command()
async def setrem(ctx, message, minutes):
  if minutes == '1':
    await ctx.send('Setting reminder "{}" to alert in {} minute'.format(message, minutes))
  else:
    await ctx.send('Setting reminder "{}" to alert in {} minutes'.format(message, minutes))
  await asyncio.sleep(int(minutes)*60)
  await ctx.send('{} Reminder: {}'.format(ctx.message.author.mention, message))

@client.command()
async def test(ctx):
  await ctx.send('tester')

# remind finishes here

client.run(os.getenv('TOKEN'))