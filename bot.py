import discord
import random
import requests
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('token')

intents = discord.Intents.all()
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix='e!', intents= intents)

@bot.command()
async def info(ctx):
    await ctx.send('Hola mundo')
    
@bot.command()
async def d4(ctx):
    dice = random.randrange(1, 5, 1)
    if dice == 1 or dice == 4:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')
    
@bot.command()
async def d6(ctx):
    dice = random.randrange(1, 7, 1)
    if dice == 1 or dice == 6:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')
    
@bot.command()
async def d8(ctx):
    dice = random.randrange(1, 9, 1)
    if dice == 1 or dice == 8:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')
    
@bot.command()
async def d10(ctx):
    dice = random.randrange(1, 11, 1)
    if dice == 1 or dice == 10:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')
    
@bot.command()
async def d12(ctx):
    dice = random.randrange(1, 13, 1)
    if dice == 1 or dice == 12:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')
    
@bot.command()
async def d20(ctx):
    dice = random.randrange(1, 21, 1)
    if dice == 1 or dice == 20:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')
    
@bot.command()
async def d100(ctx):
    dice = random.randrange(1, 101, 1)
    if dice == 1 or dice == 100:
        await ctx.send(f'¡**{dice}**!')
    else:
        await ctx.send(f'¡{dice}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'ping' in message.content.lower():
        await message.channel.send(f'pong {message.author.name}')
    
    await bot.process_commands(message)
    
url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post(url, json=data)
    
bot.run(token)