import os
import discord, json
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = "/")


# todo starts here

db = []  # or mongodb


client = commands.Bot(command_prefix = "/")



# activate via "/todo ... "
# commands:
#   /todo add [desc] [date time]
#   /todo display   (in n)
#   /tdo  
# -------------------------------
@client.command()
async def todo(ctx, arg1):
    if arg1 == "add":
        await ctx.send("toDO add")
    elif arg1 == "display":
        await ctx.send("display")
    else:
        await ctx.send("something else")

    
# ----------------------
# add arg1 to the db
# 
# ----------------------
def addToDo(arg1):


    pass


def display():
    pass

# todo finishes here

# remind starts here
@client.command()
async def setrems(ctx, message):
  await ctx.send('reminder set')
  await ctx.send(message)

# remind finishes here

client.run(os.getenv('TOKEN'))