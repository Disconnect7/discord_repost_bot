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
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!тык'):
        await message.channel.send('!тык')

@client.event
async  def on_message_edit(before, after):
    await before.channel.send('в этом канале  отредактировали сообщение')
    print(type(before))



load_dotenv()
client.run(os.getenv('TOKEN'))