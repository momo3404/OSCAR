import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json



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
async def todo(ctx, arg1):
    author = ctx.message.author

    if arg1 == "add":
        await addToDo(arg1, author)
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
# -----------------------
# displays their current todo list
# 
# -------------------
def display(author, ctx):
    for item in db[author]:
        await ctx.send(item, "\n")
        



#just putting pass so it doesnt get syntax error
# thanks!

#client.run(os.getenv('TOKEN'))