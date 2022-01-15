@client.command()
async def help(ctx):
  await ctx.send('/settimer [message] [time (minutes)] - sets a message to be displayed after a certian number of minutes')
  