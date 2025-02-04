import discord
import random
import os
from discord.ext import commands
from password import tokenn

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord bilgi botuyum!')

@bot.command()
async def bilgi(ctx):
    await ctx.send("kullanılabileceğiniz komutlar: atik,atik2,atik,3,meme")

@bot.command()
async def atik1(ctx):
    await ctx.send("1-Evdeki plastik çöpleri okuldaki el işi projelerinizde kullanabilirsiniz")

@bot.command()
async def atik2(ctx):
    await ctx.send("2-Ebeveynlerinizi bu konu hakkında uyarabilir ve öğrenmelerine yardımcı olabilirsiniz")

@bot.command()
async def atik3(ctx):
    await ctx.send("3-Evde boşuna çalışan elektrikli aletleri kapatabilirsiniz. Örneğin boşa yanan ampuller")

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run(tokenn)