async def help(ctx):
  await ctx.send('/settimer [message] [time (minutes)] - sets a message to be displayed after a certian number of minutes')
  await ctx.send('/todo add [task] - adds task to todo list')
  await ctx.send('/todo remove [task] - removes task to todo list')
  await ctx.send('/todo display - displays all current tasks on todo list')
  await ctx.send('/play [url] - starts playing music from url')
  await ctx.send('/pause - pauses current playing music')
  await ctx.send('/resume - resumes current playing music')
  await ctx.send('/stop - stops playing music')
  await ctx.send('/show [topic] - shows random image of topic')
  await ctx.send('/lily - provides motivation')
  