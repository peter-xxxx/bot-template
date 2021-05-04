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

@bot.command("8ball") # we're making an 8ball command so that it doesn't erroring
async def _ball(ctx):
    await ctx.send(random.choice(['All', 'The', '8ball', 'Responses']))

@bot.command("info") # we're creating a command with multiple lines
async def info(ctx):
    await ctx.send('This is an informational command! \n I was created by... \n My language is Python. \n My library is discord.py') # \n creates a new line without it erroring

bot.run("your token here")
