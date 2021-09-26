import random
import math
from discord import user
from discord.ext.commands.core import Command, command
import discord
import datetime
import asyncio
from discord.ext import commands


class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.exp_fake = False
        self.nuke_is_on = False
        self.senha_aceita = False

    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=['msg'])
    async def mensagem(self, ctx, *, msg):
        await ctx.channel.purge(limit=1)
        await ctx.send(msg)

    @commands.guild_only()
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx, user: discord.member.User, msg):
        await user.send(msg)
        await ctx.message.delete()

    @commands.command(aliases=['cls', 'limpar'])
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def clear(self, ctx, qnt: int):
            await ctx.channel.purge(limit=qnt + 1)

    @commands.command(aliases=['sorteio'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def giveaway(self, ctx, min: float, desc, img = None):
        await ctx.message.delete()
        embed = discord.Embed(title='Giveaway Começando!',
                              description=f'{ctx.author.mention} Está Fazendo um Giveaway de {desc}',
                              color=ctx.author.color,
                              timestamp= datetime.datetime.utcnow() + datetime.timedelta(seconds=min * 60))
        if not img == None:
            embed.set_image(url=img)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=min * 60)
        embed.set_footer(text=f'Termina em {min} minutos')
        message = await ctx.send(embed=embed)
        await message.add_reaction('🎉')
        await asyncio.sleep(min * 60)

        new_message = await ctx.channel.fetch_message(message.id)
        users = await new_message.reactions[0].users().flatten()
        users.pop(0)
        try:
            winner = random.choice(users)
        except:
            await ctx.send(f'Não há participantes no sorteio de {desc}')
        await ctx.send(f'Parabéns {winner.mention} por Ganhar **{desc}**!')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, titulo, descrição, *,  opções):
        await ctx.message.delete()
        msg = opções.split(',')
        tam = len(msg)
        if descrição == 'skip' or descrição == 'nao' or descrição == 'none':
            embed = discord.Embed(title=titulo, colour=ctx.author.color, timestamp=datetime.datetime.utcnow())
        else:
            embed = discord.Embed(title=titulo, description=descrição, colour=ctx.author.color, timestamp=datetime.datetime.utcnow())
        emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
        embed.set_footer(text=f'Votação Criada por: {ctx.author}', icon_url=ctx.author.avatar_url)

        for c in range (0, tam):
            lista = []
            embed.add_field(name=f'{msg[c]}:', value=f'Reaja com {emojis[c]}', inline=False)
            lista.append(emojis[c])
            emoji = ''
        await ctx.channel.purge(limit=1)
        mensagem = await ctx.send(embed=embed)
        for c in range(0,tam):
            await mensagem.add_reaction(emojis[c])

    @commands.command()
    async def delete_channel(self, ctx, canal:discord.TextChannel = None):
        if canal == None:
            await ctx.channel.delete()
        else:
            await canal.delete()

    @commands.command()
    async def create_channel(self, ctx, num:int, nome):
        for c in (range(1, num)):
            await ctx.guild.create_text_channel(name=nome)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member:discord.member.User, reason = None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f'Usuário {member.mention} foi banido com sucesso 👍')
        except:
            await ctx.send(f'Sla não consegui banir o {member.mention}')

def setup(client):
    client.add_cog(Mod(client))
