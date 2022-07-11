import os
import discord
import json
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# client = discord.Client() #import discord
client = commands.Bot(command_prefix='!')

repost_delay_s = 10
repost_is_not_stopped = True

#async def bf(ctx, *, args): для многих аргументов

# репостит в конкретный канал по команде
@client.command(name="тык")
async def tik(ctx):
    await ctx.send("!тык")\





@client.command(name="repost")
async def repost(ctx):
    """
        репостит сообщение во все каналы из channels_to_repost
        кроме того, а котором написано !repost...

        (что бы не присылать мем на сервер с которого его стырил)
    """

    message = ctx.message

    if trusted_author(message):
        c = 0
        for channel_id in channels_to_repost.keys():

            this_channel = message.channel
            channel = client.get_channel(int(channel_id))
            # channel = client.get_channel(991335084986744932)
            if this_channel == channel:
                pass
            else:
                try:
                    await channel.send(message.content)
                    c += 1
                except:
                    pass

        await message.author.send(f"message reposted to {c} "
                                  f"channels by !repost command")

    else:
        await respond_to(message, response=f'Вашего ID нет в моём списке '
                                           f'допущенных к щитпостингу')



@client.event
async def on_message(message):

    if message.author == client.user:  # что бы бот не общался сам с собой
        return

    if is_ZUM(message):  # немного заслуженого троллинга
        await bully_ZUM(message)
        return

    trusted_author = author_in_trusted_list(message.author.id)
    is_DM = (message.channel.type == discord.enums.ChannelType.private)

    if (trusted_author and is_DM):

        await respond_to(message, response=f"через 10 секунд будет репост")
        await asyncio.sleep(10)
        c = 0

        for channel_id in channels_to_repost.keys():

            channel = client.get_channel(int(channel_id))
            # channel = client.get_channel(991335084986744932)

            try:  # пеерсылаем сообщение, поднимем счётчик пересланых сообщений
                await channel.send(message.content)
                c += 1
            except:
                await respond_with_error(message, channel, channel_id)

        await respond_to(message, response=f'message reposted to {c} channels')

    elif(not trusted_author and is_DM):
        await respond_to(message, response=f'Вашего ID нет в моём списке '
                                     f'допущенных к щитпостингу' )

    # передать сообщение парсеру комманд, иначе on_message()
    # имеет приоритет выше любого сообщения (в том числе с любой командой)
    await client.process_commands(message)


# ______________________________________________

def trusted_author(message):
    author = message.author.id

    if str(author) in trusted_users.keys():
        return True
    else:
        return False


def author_in_trusted_list(author):
    if str(author) in trusted_users.keys():
        return True
    else:
        return False


async def respond_to(message, response):
    # отправляет сообщение {response} в канал где находится {message}
    await message.channel.send(response)


async def respond_with_error(message, channel, channel_id):
    # просто упаковка большого и бесполезного кода в отдельную функцию

    try:
        await respond_to(message, response=f"Error: can't send to: "
                                           f"'{channel.guild}   --->   {channel}' channel")
    except:
        await respond_to(message, response=f"Error: can't send to: "
                                           f"'{channel}' channel with id = {channel_id}")


def is_ZUM(message):
    # ZUM from GAYBAR guild 270184210944229381
    if message.author.id == 270184210944229381:
        return True
    else:
        return False

async def bully_ZUM(message):
    if random.random() < 0.13:
        await respond_to(message, response=f"Зум - Пидрила опять опозорился")


# ______________________________________________
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


file = open('id_users.json', 'r')
trusted_users = json.load(file)
file.close()

file = open('channels_to_repost.json', 'r')
channels_to_repost = json.load(file)
file.close()

client.run(os.getenv('TOKEN'))
