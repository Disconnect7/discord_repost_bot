import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

# client = discord.Client() #import discord
client = commands.Bot(command_prefix='!')



# репостит в конкретный канал по команде
@client.command(name="repost")
async def bf(ctx, *, args):
    if (ctx.message.author.id == 478866202371031040): # скопировать ID пользователя через ПКМ
        channal = client.get_channel(991335084986744932)
        await channal.send(ctx.message.content)

    else:
        await ctx.send(f"Вашего ID = {ctx.message.author.id} нет в списке допущенных для щитпостинга")

@client.event
async def on_message(message):
    trusted_author = (message.author.id == 478866202371031040)
    is_DM = (message.channel.type == discord.enums.ChannelType.private)
    if (trusted_author and is_DM):
        # await message.channel.send(f'message  from trusted_author and is_DM ')
        await message.channel.send(f'message reposted')

        channal = client.get_channel(991335084986744932)
        await channal.send(message.content)


def author_in_trusted_list(author):


    pass

def get_chanels_for_repost():
    pass


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(os.getenv('TOKEN'))
