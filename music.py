client = commands.Bot(command_prefix = "/")
import discord, os, youtube_dl
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


  video_settings = {}
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