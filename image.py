import os
import discord
from discord.ext import commands
import random
from googleapiclient.discovery import build

client = commands.Bot(command_prefix="/")

search_engine_id = b05c6ba6fc551be3d
api_key = AIzaSyBCvBjjP32dgS6HrYVbNmVDAVEFswsjPIU


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(q=f"{search}",
                           cx="b05c6ba6fc551be3d",
                           searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


client.run(os.getenv("TOKEN"))
