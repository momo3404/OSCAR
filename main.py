import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from remind import set_reminder

from todoList import todo

client = commands.Bot(command_prefix = "/")



client.run(os.getenv('TOKEN'))