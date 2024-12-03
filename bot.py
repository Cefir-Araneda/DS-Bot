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
async def rdice(ctx, arg):
    try:
        dice = arg.lower()
        if dice == 'd4':
            dice = random.randrange(1, 5, 1)
            if dice == 1 or dice == 4:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        elif dice == 'd6':
            dice = random.randrange(1, 7, 1)
            if dice == 1 or dice == 6:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        elif dice == 'd8':
            dice = random.randrange(1, 9, 1)
            if dice == 1 or dice == 8:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        elif dice == 'd10':
            dice = random.randrange(1, 11, 1)
            if dice == 1 or dice == 10:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        elif dice == 'd12':
            dice = random.randrange(1, 13, 1)
            if dice == 1 or dice == 12:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        elif dice == 'd20':
            dice = random.randrange(1, 21, 1)
            if dice == 1 or dice == 20:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        elif dice == 'd100':
            dice = random.randrange(1, 101, 1)
            if dice == 1 or dice == 100:
                await ctx.send(f'¡**{dice}**!')
            else:
                await ctx.send(f'¡{dice}!')
        else:
            await ctx.send('¡Elige un dado! Por ejemplo "d20"')
    except Exception as e:
        print("Error: ", e)

@rdice.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('¡Elige un dado! Por ejemplo "d20"')

@bot.command()
async def borrar(ctx, args):
    try:
        camtidad = int(args)
        await ctx.channel.purge(limit=camtidad+1)
        await ctx.send("Fueron purgados...", delete_after= 3)
    except:
        await ctx.send("Error Dx", delete_after= 3)

@borrar.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('¡Tienes que indicar cuantos mensajes!')

@bot.command()
async def purga(ctx, user: discord.User):
    def is_me(m):
        return m.author == user

    deleted = await ctx.channel.purge(limit=None, check=is_me)
    await ctx.send(f"Purgué {len(deleted)} mensajes de {user.mention}.")
    
@bot.event
async def on_ready():
    print(f'Inicio exitoso {bot.user}')
    
bot.run(token)