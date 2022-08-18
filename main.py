import os
import discord
import json
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv


client = commands.Bot(command_prefix='!')
repost_delay_s = 10
message_history_list = []



# region рабочие методы


@client.command(name="тык")
async def tik(ctx):
    await ctx.send("!тык")\


@client.command(name="delete")
async def clear_function(ctx, number_of_messages_to_delete=None):
    n = number_of_messages_to_delete

    if n == "all":
        for message in message_history_list:
            await message.delete()

        await ctx.author.send(f"!delete command was executed for 4 last indexes")

    elif n is None:
        L = last_index = len(message_history_list) - 1

        for index in range(L, L-4, -1):
            await message_history_list[index].delete()

        await ctx.author.send(f"!delete command was executed for 4 last indexes")




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
            #channel = client.get_channel(991335084986744932)
            if this_channel == channel:
                pass
            else:
                try:
                    msg = await channel.send(message.content)
                    #msg = await channel.send(f"tmp meaasge count = {c}")
                    message_history_list.append(msg)
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
    """
        репостит сообщение во все каналы из channels_to_repost

        риаботает, когда польлзователь из trusted_users
        отправляет DM (приватное сообщение) боту

        удобно тем что не нужно писать никакую комманду,
        бот сразу репостит мемы
    """

    if message.author == client.user:  # что бы бот не общался сам с собой
        return

    if is_ZUM(message):  # немного заслуженого троллинга
        await bully_ZUM(message)
        return

    # сообщение было написано боту в личку
    is_DM = (message.channel.type == discord.enums.ChannelType.private)

    if trusted_author(message) and is_DM:

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

# endregion

#region вспомогательные методы


def trusted_author(message):
    author = message.author.id

    if str(author) in trusted_users.keys():
        return True
    else:
        return False


def repost_message_in_all_unmuted_channals():
    """
    repost messages,
    and add a list of  [ms1, ms2, ms3 ...] in the end of message_history_list

    bebebe be bebebebe
    """
    pass

def show_list_of_servers_to_repost():
    """
    print numbered list of "unmuted" servers/channels
    {repost_message_in_all_unmuted_channals}

    (in which ones can repost messages now)
    """
    pass

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


#endregion

# region настройка и запуск бота


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# загружаем ID юзеров бота из файла
file = open('id_users.json', 'r')
trusted_users = json.load(file)
file.close()

# загргужаем ID каналов куда будем репостить мемы
file = open('channels_to_repost.json', 'r')
channels_to_repost = json.load(file)
file.close()

load_dotenv()
#client.run(os.getenv('TOKEN'))

# endregion

if __name__ == '__main__':
    plm = os.getenv("ПЕЛЬМЕНИ")


    print(type(plm))
    print(plm)
