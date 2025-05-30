import discord, os, random, requests, asyncio
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def senyum(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def koin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def warna(ctx):
    await ctx.send(gen_color())

@bot.command()
async def heart(ctx):
    await ctx.send("❤️❤️❤️")

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def tolong(ctx):
    await ctx.send('Commands : $hello, $senyum, $koin, $warna, $heart, $pasw, $meme, $duck, $polusi, timer')

@bot.command()
async def meme(ctx):
    #with open('images/meme1.jpg', 'rb') as f:
        #picture = discord.File(f)

    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def polusi(ctx):
    with open('solusi.txt', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())
    with open('sampah/sampah.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    fact_name = random.choice(os.listdir('facts'))
    with open(f'facts/{fact_name}', 'r', encoding='utf-8') as f:
        await ctx.send(f.read())

@bot.command()
async def timer(ctx, detik: int):
    await ctx.send(f"Timer dimulai selama {detik} detik!")
    await asyncio.sleep(detik)
    await ctx.send("⏰ Timer selesai!")

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")
