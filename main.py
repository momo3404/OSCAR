import os
import discord, json, platform, youtube_dl  # removed nacl
import time, asyncio, datetime
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import Bot

import random
from googleapiclient.discovery import build

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
        # need to get all the string
        todo_string = makeString(arg)
        addToDo(todo_string, author)
        await ctx.send("added!")
    elif arg[0] == "display":  
        await ctx.send("displaying...")
        # temporariry display them like this
        i_ = 1
        for item in db[author]:
            await ctx.send("%d. %s" % (i_, item["name"]))
            i_ += 1
    elif arg[0] == "remove":
        print("line 56")
        remove(arg, author)
    else:
        await ctx.send("something else")

# -------------
# concatenate all the parameter
def makeString(arg):
    s = arg[1]
    for i in range(2, len(arg)):
        s += " " + arg[i]
    return s

# -------------------
# remove
def remove(arg, author):
    list_todo = db[author]
    # remove all todo list at that index
    # super inefficient method
    newlist = []
    removeIndices = arg[1:]  # indexes to remove
    # conver elment to int
    removeIndices = list(map(int , removeIndices))  
    print(arg)
    print(removeIndices)
    for i in range(0, len(list_todo)):
        if (i + 1) not in removeIndices:
            newlist.append(list_todo[i])
    db[author] = newlist  # new list with removed indices
    print("line 81")
   

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



#image.py starts here

@client.command()
async def lily(ctx, *arg):
  await ctx.send(file=discord.File("lily-2.jpg"))

api_key = "AIzaSyBCvBjjP32dgS6HrYVbNmVDAVEFswsjPIU"


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    random_value = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(q=f"{search}",
                           cx="b05c6ba6fc551be3d",
                           searchType="image").execute()
    url = result["items"][random_value]["link"]
    embed1 = discord.Embed(title=f"Here is a ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


# image.py ends here


# music.py starts here

@client.command()
async def play(ctx, url):
  song = os.path.isfile("song.mp3")
  try:
    if song:
      os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Wait for the current playing music to end or use the 'stop' command")
    return
  
  voice_channel = discord.utils.get(ctx.guild.voice_channels, name = 'music')
  await voice_channel.connect()
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)


  video_settings = {
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
          }],
      }
  with youtube_dl.YoutubeDL(video_settings) as ydl:
    ydl.download([url])

  for file_name in os.listdir("./"):
    if file_name.endswith(".mp3"):
      os.rename(file_name, "music.mp3")
  voice.play(discord.FFmpegPCMAudio("music.mp3"))


  @client.command()
  async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_paused():
      voice.resume()

  @client.command()
  async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_connected():
      await voice.disconnect()

  @client.command()
  async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_playing():
      voice.pause()
# music.py ends here

# commands.py starts here
@client.command()
async def commands(ctx):
  await ctx.send("OSCAR Bot Commands:")
  await ctx.send("/settimer [message] [time (minutes)] - sets a message to be displayed after a certian number of minutes")
  await ctx.send('/todo add [task] - adds task to todo list')
  await ctx.send('/todo remove [task] - removes task to todo list')
  await ctx.send('/todo display - displays all current tasks on todo list')
  await ctx.send('/play [url] - starts playing music from url')
  await ctx.send('/pause - pauses current playing music')
  await ctx.send('/resume - resumes current playing music')
  await ctx.send('/stop - stops playing music')
  await ctx.send('/lily - provides motivation')
  
# commands.py ends here
client.run(os.getenv("TOKEN"))