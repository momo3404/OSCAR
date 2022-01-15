import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot



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
    return

client.run(os.getenv('TOKEN'))
    




