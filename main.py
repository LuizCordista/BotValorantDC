import os

import discord
from discord.ext import commands

from valorant_api import elovalorant

secret = os.environ["Token_key"]

intents = discord.Intents.all() 

client = commands.Bot(command_prefix = "/", intents=intents)

@client.event
async def on_ready(self):
    print(f"Logado como {self}")

@client.command()
async def valorantelo(ctx, name, tag):
  embed = discord.Embed(
    colour=discord.Colour.gold(),
    title=f"{name}: {elovalorant(name, tag)[0]}",
    description=f"{elovalorant(name, tag)[1]} pontos"
  )
  embed.set_thumbnail(url=elovalorant(name, tag)[2])
  await ctx.send(embed=embed)

client.run(secret)
