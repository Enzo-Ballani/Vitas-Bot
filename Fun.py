import asyncio
import random
import os
import discord
from discord.ext import commands
import datetime
import main

class Fun(commands.Cog):


    def __init__(self, client):
        self.client = client

        #variaveis da luta
        self.p1 = discord.User
        self.p2 = discord.User
        self.round = discord.User
        self.p1Life = 100
        self.p2Life = 100
        self.is_on_fight = False
        self.accepted = False
        self.recused = False

    #meme
    @commands.command()
    async def meme(self, ctx, número=None):
        limite = 90
        if número == None:
            await ctx.send(f'Meme aleatório saindo para: {ctx.author.mention}')
            lista = []
            for c in range(1, limite + 1):
                lista.append(c)
            ran = random.choice(lista)
            meme = f'./Memes/{ran}.mp4'
            await ctx.send(file=discord.File(meme))
            teste = [1, 2, 3, 4]
            yn = random.choice(teste)
            if yn == 1:
                embed = discord.Embed(title='Sabia Que Você Pode Escolher Qual Meme Eu Mando?',
                                      description='Só Colocar Um Número Após o ".meme"',
                                      colour=discord.colour.Colour.random())
                await ctx.send(embed=embed)
        else:
            número = int(número)
            if número < 1:
                await ctx.send('Não Coloque Números Menores Que 1')
                print(f'{ctx.author} tentou usar o Comando "MEME" com um número menor que 1')
            elif número == 666:
                await ctx.send(files=discord.File('./Memes/666.mp4'))

            elif número > limite:
                await ctx.send(f'Só Tenho {limite} Memes')
                print(f'{ctx.author} Tentou usar o Comando "MEME" com um número maior que {limite}')
            else:
                await ctx.send(f'Meme número {número} saindo para: {ctx.author.mention}')
                meme = f'./Memes/{número}.mp4'
                await ctx.send(file=discord.File(meme))
                print(f'{ctx.author} usou o Comando "MEME" com o número {número} no {ctx.channel}')

    @commands.command(aliases=['_.', '-.'])
    async def piadocas(self, ctx):
        await ctx.send('Para de usar carinhas seu puto')

    @commands.command(aliases=['fight', 'briguinha'])
    @commands.guild_only()
    async def luta(self, ctx, adversário:discord.User):
        if not ctx.author == adversário:
            if not self.is_on_fight:
                self.is_on_fight = True
                await ctx.send(f'Eita {adversário.mention} acho que você foi DESAFIADO!!!!!!\nDiga "sim" para aceitar')
                self.p1 = ctx.author
                self.p2 = adversário

                await asyncio.sleep(8)
                if self.accepted:
                    self.comandos = '``Fugir``: Fuja da batalha igual um covarde\n \n``Cura``: Cure 20 de vida e fique na vantagem\n \n``Soco``: Soque a cara do adversário tirando de 10 a 20 de vida, 100% de chance de acertar\n \n``Chute``: Chuta o saco dessa vagabunda tirando de 10 a 40 de vida, 75% de chance  de acertar\n \n``hadouken``: Ataque forte, hitkill, 10% de chance de acertar'
                    self.round = self.p1
                    embed = discord.Embed(title='Comandos de Batalha:',
                                          colour=ctx.author.colour,
                                          description=f'**{self.comandos}**')
                    await ctx.send(embed=embed)
                    await ctx.send(f'{self.round.mention} começa!')
                elif self.recused:
                    await ctx.send(f'{adversário.mention} recusou a luta, acho que ele é ruim')
                    self.recused = False
                else:
                    await ctx.send(f'{adversário.mention} amarelou')
                    self.is_on_fight = False
                    self.accepted = False

            else:
                await ctx.send('Uma luta já foi iniciada')
        else:
            await ctx.send(f'{ctx.author.mention} se acertou com uma pá e agora está internado no SUS. Não foi uma boa escolha.l')

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.is_on_fight:
            if message.content.lower() == 'sim' and message.author == self.p2:
                self.accepted = True
            if message.content.lower() == 'nao' or message.content.lower() == 'não' and message.author == self.p2:
                self.recused = True
                self.is_on_fight = False
                self.accepted = False

            if self.accepted:
                if message.content.lower() == 'fugir':
                    if message.author == self.p1:
                        await message.channel.send(f'{self.p1.mention} fugiu da batalha KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
                        self.accepted = False
                        self.recused = True
                        self.is_on_fight = False
                        self.p1Life = 100
                        self.p2Life = 100
                    if message.author == self.p2:
                        await message.channel.send(f'{self.p2.mention} fugiu da batalha KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
                        self.accepted = False
                        self.recused = True
                        self.is_on_fight = False
                        self.p1Life = 100
                        self.p2Life = 100

                if message.content.lower() == 'cura' and message.author == self.round:
                    if self.round == self.p1 and message.author == self.round:
                        if self.p1Life <= 80:
                            self.p1Life += 20
                            await message.channel.send(f'💊 {self.round.mention} curou 20 de vida, ficando com {self.p1Life}')
                            self.round = self.p2
                        else:
                            await message.channel.send('❌ Muita Vida, não é possível se curar\nTente Outro Comando')

                    if self.round == self.p2 and message.author == self.round:
                        if self.p2Life <=80:
                            self.p2Life += 20
                            await message.channel.send(f'💊 {self.round.mention} curou 20 de vida, ficando com {self.p2Life}')
                            self.round = self.p1
                        else:
                            await message.channel.send('❌ Muita Vida, não é possível se curar\nTente Outro Comando')


                if message.content.lower() == 'soco' and message.author == self.round:
                    if self.round == self.p1 and message.author == self.round:
                        self.p2Life -= random.choice(range(10, 20))
                        if self.p2Life >0:
                            await message.channel.send(f'👊 {self.p1.mention} socou {self.p2.mention}, deixando-o com {self.p2Life}')
                            self.round = self.p2
                        else:
                            await message.channel.send(f'🏆 {self.p1.mention} nocauteou {self.p2.mention}. Boa!!!')
                            self.accepted = False
                            self.recused = True
                            self.is_on_fight = False
                            self.p1Life = 100
                            self.p2Life = 100


                    if self.round == self.p2 and message.author == self.round:
                        self.p1Life -= random.choice(range(10, 20))
                        if self.p1Life >0:
                            await message.channel.send(f'👊 {self.p2.mention} socou {self.p1.mention}, deixando-o com {self.p1Life}')
                            self.round = self.p1
                        else:
                            await message.channel.send(f'🏆 {self.p2.mention} nocauteou {self.p1.mention}. Boa!!!')
                            self.accepted = False
                            self.recused = True
                            self.is_on_fight = False
                            self.p1Life = 100
                            self.p2Life = 100

                if message.content.lower() == 'chute' and message.author == self.round:
                    if self.round == self.p1 and message.author == self.round:
                        chance = random.choice(range(1,100))
                        if chance > 25:
                                self.p2Life -= random.choice(range(10, 40))
                                if self.p2Life < 0:
                                    await message.channel.send(f'🏆 {self.p1.mention} deixou {self.p2.mention} com traumatismo crâniano depois desse chute kkkk')
                                    self.accepted = False
                                    self.recused = True
                                    self.is_on_fight = False
                                    self.p1Life = 100
                                    self.p2Life = 100
                                else:
                                    await message.channel.send(f'🦶 {self.p1.mention} deixou {self.p2.mention} com {self.p2Life} de vida')
                                    self.round = self.p2
                        else:
                            await message.channel.send(f'❌ {self.p1.mention} errou o chute')
                            self.round = self.p2

                    if self.round == self.p2 and message.author == self.round:
                        chance = random.choice(range(1,100))
                        if chance > 25:
                                self.p1Life -= random.choice(range(25, 40))
                                if self.p1Life < 0:
                                    await message.channel.send(f'🏆 {self.p2.mention} deixou {self.p1.mention} com traumatismo crâniano depois desse chute kkkk')
                                    self.accepted = False
                                    self.recused = True
                                    self.is_on_fight = False
                                    self.p1Life = 100
                                    self.p2Life = 100
                                else:
                                    await message.channel.send(f'🦶 {self.p2.mention} deixou o {self.p1.mention} com {self.p1Life} de vida')
                                    self.round = self.p1
                        else:
                            await message.channel.send(f'❌ {self.p2.mention} errou o chute')
                            self.round = self.p1

                if message.content.lower() == 'hadouken' and message.author == self.round:
                    if self.round == self.p1 and message.author == self.round:
                        chance = random.choice(range(1,100))
                        if chance > 80:
                                await message.channel.send(f'🏆 {self.p1.mention} acertou um Hadouken com 10% de chance, muito bom')
                                self.accepted = False
                                self.recused = True
                                self.is_on_fight = False
                                self.p1Life = 100
                                self.p2Life = 100
                        else:
                            await message.channel.send(f'❌ {self.p1.mention} errou o hadouken')
                            self.round = self.p2

                    if self.round == self.p2 and message.author == self.round:
                        chance = random.choice(range(1, 100))
                        if chance > 80:
                            await message.channel.send(f'🏆 {self.p2.mention} acertou um Hadouken com 10% de chance, muito bom')
                            self.accepted = False
                            self.recused = True
                            self.is_on_fight = False
                            self.p1Life = 100
                            self.p2Life = 100
                        else:
                            await message.channel.send(f'❌ {self.p2.mention} errou o hadouken')
                            self.round = self.p1

                if message.content.lower() == 'vida':
                    embed = discord.Embed(title='**Vida dos Jogadores**',
                                          colour=discord.Colour.red())
                    embed.add_field(name=f'Jogador 1: {self.p1}', value=f'{self.p1Life} de vida', inline=False)
                    embed.add_field(name=f'Jogador 1: {self.p2}', value=f'{self.p2Life} de vida', inline=False)
                    await message.channel.send(embed=embed)

                if message.content.lower() == 'comandos':
                    embed = discord.Embed(title='Comandos de Batalha:',
                                          colour=ctx.author.colour,
                                          description=f'**{self.comandos}**')
                    await message.channel.send(embed=embed)
                    await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))