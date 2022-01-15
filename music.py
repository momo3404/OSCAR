client = commands.Bot(command_prefix = "/")

@client.command()
async def play(ctx, url):
  song = os.path.isfile("music.mp3")
  try:
    if song:
      os.remove("music.mp3")
    return
  
  voice_channel = discord.utils.get(ctx.guild.voice_channels, name = "music")
  await voice_channel.connect()
  voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

  @client.command()
  async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_paused():
      voice.resume()
    

  @client.command()
  async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if voice.is_connected():
      await voice.disconnect