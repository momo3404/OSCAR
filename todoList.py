import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json



db = dict()  # or mongodb


"""
dictionnary of <string, List<dict<string, string>>>
db = {
    "user1": [{"name": "todo1"}, "name": "todo2", ...]
    "user2": []
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


    # need to get all the string
    todo_string = makeString(arg)

    print(author)
    if arg[0] == "add":
        addToDo(todo_string, author)
        await ctx.send("added!")
    elif arg[0] == "display":  
        await ctx.send("displaying...")
        # temporariry display them like this
        for item in db[author]:
            await ctx.send("%s" % item)
    elif arg[0] == "remove":
        remove(arg, author)
    else:
        await ctx.send("something else")


# -------------------
# remove
def remove(arg, author):
    list_todo = db[author]
    # remove all todo list at that index
    # super inefficient method
    newlist = []
    removeIndices = arg[1:]  # indexes to remove
    for i in range(0, len(list_todo)):
        if (i + 1) not in removeIndices:
            newlist.append(list_todo[i])
    db[author] = newlist  # new list with removed indices
    


# -------------
# concatenate all the parameter
def makeString(arg):
    s = arg[1]
    for i in range(2, len(arg)):
        s += " " + arg[i]
    return s
    
# ----------------------
# add msg to the db written by author
# 
# ----------------------
def addToDo(msg, author):
    if (author in db.keys()):  # user exist
        if {"name": msg} not in db[author]:
            db[author].append({"name": msg})
    else: # case: this is new person
        db[author] = [{"name": msg}]
# -----------------------
# displays their current todo list
# 
# -------------------
def display(author, ctx):
    pass



#just putting pass so it doesnt get syntax error
# thanks!

#client.run(os.getenv('TOKEN'))