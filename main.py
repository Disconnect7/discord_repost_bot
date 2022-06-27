"""
import os

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='сасат')
async def sasat_function(ctx):

    response = "сасат! sasat? сасатъ, САСАТ, сасат?!"
    await ctx.send(response)

bot.run(TOKEN)
"""
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

#client = discord.Client()
client = commands.Bot(command_prefix='!')


@client.command(name="id")
async def id(ctx):
    message = ctx.message
    await message.channel.send("Your id = " + str(message.id))

@client.command(name="bruh")
async def abc(ctx, arg1=None, arg2=None):

    if (arg1 or arg2):
        await ctx.send("bruh command with benefits")
        await ctx.send(f"type(arg1) = {type(arg1)}\ntype(arg2) = {type(arg2)}")
    else:
        await ctx.send("just bruh command")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

"""
# on_message() перебивает по приоритету @client.command()
# :sadporo:

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!тык'):
        await message.channel.send('!тык')
"""

@client.event
async def on_message_edit(before, after):
    await before.channel.send('в этом канале  отредактировали сообщение')
    print(type(before))


load_dotenv()
client.run(os.getenv('TOKEN'))
