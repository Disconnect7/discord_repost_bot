import os
import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

# client = discord.Client() #import discord
client = commands.Bot(command_prefix='!')




# репостит в конкретный канал по команде
@client.command(name="repost")
async def bf(ctx, *, args):
    if (ctx.message.author.id == 478866202371031040): # скопировать ID пользователя через ПКМ
        channel = client.get_channel(991335084986744932)
        await channel.send(ctx.message.content)

    else:
        await ctx.send(f"Вашего ID = {ctx.message.author.id} нет в списке допущенных для щитпостинга")


@client.event
async def on_message(message):

    if message.author == client.user:  # что бы бот не общался сам с собой
        return

    trusted_author = author_in_trusted_list(message.author.id)
    is_DM = (message.channel.type == discord.enums.ChannelType.private)

    if (trusted_author and is_DM):

        c = 0

        for channel_id in channels_to_repost.keys():

            channel = client.get_channel(int(channel_id))
            # тык # channel = client.get_channel(991335084986744932)

            try:  # пеерсылаем сообщение, поднимем счётчик пересланых сообщений
                await channel.send(message.content)
                c += 1
            except:
                await message.channel.send(f"Error: can't send to: "
                                           f"'{channel.guild}   --->   {channel}' channel")

        await message.channel.send(f'message reposted to {c} channels')



    elif(not trusted_author and is_DM):
        await message.channel.send(f'Вашего ID нет в моём списке '
                                   f'допущенных к щитпостингу')


def author_in_trusted_list(author):
    if str(author) in trusted_users.keys():
        return True
    else:
        return False


def respond_to(message, response):
    await message.channel.send(response)


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
