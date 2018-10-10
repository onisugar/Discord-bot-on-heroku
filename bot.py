import discord
import requests
from discord.ext import commands
import asyncio
import os


#GIVE YOUR BOT A PREFIX; mine is a.
bot = commands.Bot(command_prefix="!")




#PRINT THE DISCORD BOT'S NAME WHEN IT'S READY
@bot.event
async def on_ready():
      print(bot.user.name)

        
#A SIMPLE TEST COMMAND
@bot.command(pass_context=True)
async def hi(ctx):
      await bot.say("Hello there"+" "+ctx.message.author.name)


@bot.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = request.get(url)
    value = response.json() ['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" +value)
                  
                   
#YOU CAN USE os.environ TO HIDE YOUR BOT TOKEN: SAVE YOUR BOT TOKEN AS THE NAME YOU GAVE IN os.environ['name'] 
bot.run(os.environ['BOT_TOKEN'])
