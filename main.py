import os
import discord, json, platform, nacl, youtube_dl
import time, asyncio, datetime
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = "/")


# todo starts here

db = dict()  # or mongodb
"""
dictionnary of <string, sets<string>>
db = {
    "user1": {"todo1", "todo2", ...}
    "user2": {}
    .
    .
    .
}

"""

client = commands.Bot(command_prefix = "/")



# activate via "/todo ... "
# commands:
#   /todo add [desc] [date time]
#   /todo display   (in n)
#   /tdo  
# -------------------------------
@client.command()
async def todo(ctx, *arg):
    author = ctx.message.author
    print(author)
    if arg[0] == "add":
        addToDo(arg[1], author)
        await ctx.send("added!")
    elif arg[0] == "display":  # TODO: @ethanlim
        await ctx.send("displaying...")
        # temporariry display them like this
        for item in db[author]:
            await ctx.send("%s" % item)
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


# print to terminal for debug
def printDisplay_consol():
    print(db)

# todo finishes here

# remind starts here
@client.command()
async def settimer(ctx, message, minutes):
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