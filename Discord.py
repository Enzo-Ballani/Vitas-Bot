import discord
from discord.ext import commands
import random
import main
import datetime

class Discord(commands.Cog):
    def __init__(self, client):
        self.client = client

    #avatar
    @commands.guild_only()
    @commands.command(aliases=['avt', 'foto'])
    async def avatar(self, ctx, user:discord.member.User = None):
        lista = ['Bixo Feio',
                 'Ele é semi-gay',
                 'Meu dia Já Estava Ruim\nDepois de Ver Isso Parece que Piorou',
                 'Grande Obra de Arte Feita pelo Demônio 😍😍😍']
        if user == None or user == ctx.author:
            embed = discord.Embed(title=f'Seu Avatar {ctx.author}', description= f'{random.choice(lista)}\n \n Baixe a sua Foto [Aqui]({ctx.author.avatar_url})', colour=ctx.author.color)
            embed.set_image(url=ctx.author.avatar_url)
            if user == ctx.author:
                embed.set_footer(text='Não Precisa se marcar para ver sua foto')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f'O Avatar de {user.display_name}, como você pediu', description=f'{random.choice(lista)} \n \n Baixe a Foto [Aqui]({user.avatar_url})',colour=user.colour)
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text=f'A Pedido de {ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        # user_info
        @commands.command(aliases=['userinfo', 'usr_if', 'hack'])
        async def user_info(self, ctx, user: discord.member.User = None):
            if user == None or user.name == ctx.author:
                embed = discord.Embed(title=f'Suas Informações {ctx.author.display_name}',
                                      colour=ctx.author.color,
                                      timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=ctx.author.avatar_url)
                fields = [('Seu Nome Real', ctx.author.name, False),
                          ('Seu ID', ctx.author.id, False),
                          ('Seu Cargo Mais Alto', ctx.author.top_role.mention, False),
                          ('Você Criou a Conta no Dia:', ctx.author.created_at.strftime("%d/%m/%Y as %H:%M:%S"), True),
                          ('Você Entrou Nesse Servem no Dia:', ctx.author.joined_at.strftime("%d/%m/%Y as %H:%M:%S"),
                           True),
                          ]
                if user == None:
                    pass
                else:
                    embed.set_footer('Você não precisa se marcar para ver suas informações')
            else:
                embed = discord.Embed(title=f'Informações do Usuário {user.display_name}',
                                      colour=user.colour,
                                      timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=user.avatar_url)
                fields = [('Nome Real', user.name, False),
                          ('ID', user.id, False),
                          ('Cargo Mais Alto', user.top_role.mention, False),
                          ('Essa Conta foi Criada Dia:', user.created_at.strftime("%d/%m/%Y as %H:%M:%S"), True),
                          ('Essa Conta Entrou No Server Dia:', user.joined_at.strftime("%d/%m/%Y as %H:%M:%S"), True),
                          ]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Discord(client))