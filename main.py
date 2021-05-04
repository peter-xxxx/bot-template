import discord
from discord import utils
from discord.ext import commands
import random 
# we're importing all the modules we need

intents = discord.Intents(messages = True)

bot = commands.Bot(command_prefix = 'Your Prefix', intents = intents, status = discord.Status.online, activity = discord.Game("You're status message here"))
# this tells discord.py what our prefix will be (use ['Prefix 1', 'Prefix 2', 'etc'] for multiple prefixes. Replace "You're status message here" with what you want your bots status to be.

@bot.command("ping") # we're making a command  
async def ping(ctx):
    await ctx.send("Pong!") # make sure your indentation is right! Our bot will return whatever you put inside the "".

@bot.command("coin") # we're making a command that returns a random choice from a list
async def coin(ctx):
    await ctx.send(random.choice(['Heads', 'Tails'])) # your bot will choose either 'heads' or 'tails'.

bot.run("your token here")
