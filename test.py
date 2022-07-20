import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# client = discord.Client() #import discord
client = commands.Bot(command_prefix='!')


# async def function_name(ctx, *, args): для многих аргументов


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

@client.command(name="Дисконнект")
async def bf(ctx, *, args):
    if (ctx.message.author.id == 478866202371031040): # скопировать ID пользователя через ПКМ
        await ctx.send(f"Определённо ты, {ctx.message.author}")
    else:
        await ctx.send("Я не знаю")
        await ctx.send(f"Your id = {str(ctx.message.author.id)}\n"
                       f"ctx.message.author.id == id: {ctx.message.author.id == 478866202371031040}")

@client.command(name="meme")
async def bf(ctx):
    m = "https://cdn.discordapp.com/attachments/4383858" \
         "99873763328/990366770172944444/unknown.png"
    await ctx.send(m)


@client.command(name="send")
async def bf(ctx):
    channal = client.get_channel(991335084986744932) # скопировать ID текстового канала с ботом через ПКМ
    await channal.send(f"sendind messege in text channal with ID 991335084986744932")

@client.command(name="TypeOfChannal")
async def bf(ctx):
    await ctx.send(f"ctx.message.channel = {ctx.message.channel}")
    await ctx.send(f"ctx.message.channel.type = {ctx.message.channel.type }")

'''
# on_message() перебивает по приоритету @client.command()
# :sadporo:

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!тык'):
        await message.channel.send('!тык')
'''

@client.event
async def on_message_edit(before, after):
    await before.channel.send('в этом канале  отредактировали сообщение')
    print(type(before))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(os.getenv('TOKEN'))

print(123)
