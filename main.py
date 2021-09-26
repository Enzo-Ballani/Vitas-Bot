import asyncio
import time
import os
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import AutoShardedBot
import random

client = AutoShardedBot(command_prefix='.', case_insensitive=True)
cogs = ['Fun', 'Discord', 'Mod']

token = input('Token do Bot')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando Inválido. Tente Novamente')
    else:
        print(error)
        pass

@client.event
async def on_ready():
    'status_loop.start()'
    print('\033[34m-=\033[m' * 20)
    print(f'\033[32mBot {client.user.name} Iniciado com Sucesso !')
    print(f'Seu ID: {client.user.id}')
    print(f'Você Está em {len(client.guilds)} servers:')
    for c in client.guilds:
        print(c)
    print('\033[34m-=\033[m' * 20)

async def status():
    await client.wait_until_ready()
    statuses = ['EU TO VIVO PORRA', 'Finalmente o preguiçoso do Ballani procurou resolver', 'Ainda mais forte e mais Bonito']
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

        await asyncio.sleep(15)
client.loop.create_task(status())

@client.event
async def on_member_join(member):   
    print(f'{member} entrou no servidor.')
    channel = client.get_channel(823546618862108707)
    mgs = await channel.send(f'Bom Dia {member.mention} <:mestre:841443673043501106>')

@client.event
async def on_member_remove(member):
    print(f'{member} saiu do servidor.')

for c in cogs:
    for c in cogs:
        try:
            client.load_extension(c)
            print(f'Módulo {c} Está Ativo')
            time.sleep(0.2)
        except:
            pass

print('Iniciando o Bot . . .')

client.run(token)