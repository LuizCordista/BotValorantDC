import os

import discord
from discord.ext import commands

from valorant_api import eloluoz, elorandom

segredinho = os.environ["Token_key"]

intents = discord.Intents.all() 

client = commands.Bot(command_prefix = "/", intents=intents)

@client.event
async def on_ready(self):
    print(f"Logado como {self}")

@client.command()
async def teste(ctx):
    await ctx.send("Testando o bot aqui") 

@client.command()
async def master(ctx):
    await ctx.send("Master o mais trouxa desse servidor")

@client.command()
async def anamon(ctx):
    await ctx.send("A mais bela")

@client.command()
async def tardelli(ctx):
    await ctx.send("Leleo, vulgo: amaratos, amarantes, love rats e rato.")

@client.command()
async def luozelo(ctx):
  embed = discord.Embed(
    colour=discord.Colour.gold(),
    title=f"Luoz: {eloluoz()[0]}",
    description=f"{eloluoz()[1]} pontos"
  )
  embed.set_thumbnail(url=eloluoz()[2])
  await ctx.send(embed=embed)

@client.command()
async def elovalorant(ctx, name, tag):
  embed = discord.Embed(
    colour=discord.Colour.gold(),
    title=f"{name}: {elorandom(name, tag)[0]}",
    description=f"{elorandom(name, tag)[1]} pontos"
  )
  embed.set_thumbnail(url=elorandom(name, tag)[2])
  await ctx.send(embed=embed)

client.run(segredinho)
