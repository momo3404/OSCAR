import os
import discord, json, platform, youtube_dl  
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
#   /todo add [desc] [time] where time = _m/_h/_w/_m/_y
#   /todo display   (in list)
#   /todo remove [list of index to remove] 
# -------------------------------
@client.command()
async def todo(ctx, *arg):
    author = ctx.message.author
    print(author)
    if arg[0] == "add":
        lastarg = arg[-1]
        valid = ["h", "w", "m", "y", "d"]

        num = lastarg[:-1]  # time flag
        try:  # check if the time they entered is valid
            num = int(num)
            if (lastarg[-1] not in valid):
                print("invalid line 51")
                await ctx.send("invalid add format, please do /commands")
                return
        except:
            print("invalid line 55")
            await ctx.send("invalid add format, please do /commands")
            return
        minutes = computeMinute(lastarg) 
        # need to get all the string
        todo_string = makeString(arg[:-1]) # extract the task string
        addToDo(todo_string, author)
        await ctx.send("added!")
        await ctx.invoke(client.get_command('settimer'), message=todo_string, minutes=minutes)  # call "settimer" method
        print("line 49")
    elif arg[0] == "display":  
        await ctx.send("displaying...")
        if (author not in db.keys()):
            await ctx.send("no tasks in todo list")
            return
        if (len(db[author]) == 0):
            await ctx.send("no tasks in todo list")
            return

        # temporariry display them like this
        i_ = 1
        for item in db[author]:
            await ctx.send("%d. %s" % (i_, item["name"]))
            i_ += 1
        
    elif arg[0] == "remove":
        if (author not in db.keys()):
            await ctx.send("todo list empty, can't remove anything")
            return
        if (len(db[author]) == 0):
            await ctx.send("todo list empty, can't remove anything")
            return
        flag = remove(arg, author)
        if (flag == False):
            await ctx.send("invalid task to remove, please use index (1...) within range")
            return
        if (flag == "invalid arg"):
            await ctx.send("please choose the index to remove")
            return

        await ctx.send("removed! current tasks..")
        i_ = 1
        for item in db[author]:
            await ctx.send("%d. %s" % (i_, item["name"]))
            i_ += 1
    else:
        await ctx.send("something else")

def computeMinute(time_):
    if (time_[-1] == 'h'):  # case: __hour
        # hour to minute
        time_string = time_[: -1]  # everying but last char
        time_int = int(time_string)
        return time_int * 60
    elif (time_[-1] == "w"):  # case: __ week
        time_string = time_[: -1]
        time_int = int(time_string)
        return time_int * 10080
    elif (time_[-1] == "m"): # case: __mimutes
        time_string = time_[:-1]
        time_int = int(time_string)
        return time_int
    elif (time_[-1] == "y"):  #c case: __ year
        time_string = time_[:-1]
        time_int = int(time_string)
        return time_int * 525600
    elif (time_[-1] == "d"):  #case: __day
        time_string = time_[:-1]
        time_int = int(time_string)
        return time_int * 1440

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
    if (len(removeIndices) == 0):
        return "invalid arg"
    # conver elment to int
    for index in removeIndices:
        # index out of bound check
        if int(index) > (len(list_todo)):
            return False
        elif int(index) < 1:
            return False
    removeIndices = list(map(int , removeIndices))  
    for i in range(0, len(list_todo)):
        if (i + 1) not in removeIndices:
            newlist.append(list_todo[i])
    db[author] = newlist  # new list with removed indices

    return True

   

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
    embed1 = discord.Embed(title=f"Here is a(n) {search.title()}")
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
  await ctx.send("/settimer [message] [time (minutes)] - sets a message to be displayed after a certain number of minutes")
  await ctx.send('/todo add [task] [time]- adds task to todo list [time]: _w, _h, _m, _y, _d')
  await ctx.send('/todo remove [task] - removes task to todo list. [task]: type a number between 1 and higher ')
  await ctx.send('/todo display - displays all current tasks on todo list')
  await ctx.send('/play [url] - starts playing music from url')
  await ctx.send('/pause - pauses current playing music')
  await ctx.send('/resume - resumes current playing music')
  await ctx.send('/stop - stops playing music')
  await ctx.send('/show [topic] - shows random image of topic')
  await ctx.send('/lily - provides motivation')
  
# commands.py ends here
client.run(os.getenv("TOKEN"))