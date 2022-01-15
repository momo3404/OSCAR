import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json



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
client.run(os.getenv('TOKEN'))
    
# ----------------------
# add arg1 to the db
# 
# ----------------------
def addToDo(arg1):


    pass


def display():
    pass

#just putting pass so it doesnt get syntax error
# thanks!

