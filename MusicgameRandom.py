import discord
from discord.ext import commands
from discord import app_commands
import random
import sqlite3

TOKEN = 'YOUR_TOKEN'
intent = discord.Intents.all()
client = discord.Client(intents=intent)
tree = discord.app_commands.CommandTree(client)
dbname = "Musicgame.db"

def get_random_entry_from_db(model, level):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM musicgame WHERE model = ? AND level = ?", (model, level))
    rows = cursor.fetchall()
    
    conn.close()
    
    if rows:
        return random.choice(rows)
    else:
        return None

@tree.command(name="nya", description="にゃーん")
async def nya(ctx:discord.Interaction):
    await ctx.response.send_message("にゃーん")

@tree.command(name="random_aisatu", description="ランダムで挨拶を返してくれます")
async def random_aisatu(ctx:discord.Interaction):
    aisatu = ["こんにちは！",
    "やあ！",
    "おはようございます！",
    "こんばんは！",
    "ハロー！",
    "元気ですか？"]
    aisatu_ran = random.choice(aisatu)
    await ctx.response.send_message(aisatu_ran)

@tree.command(name="write_aisatu", description="書いた挨拶を返してくれます", guild=discord.Object(id=YOUR_GUILT_ID))
async def write_aisatu(ctx:discord.Interaction, aisatu:str):
    await ctx.response.send_message(aisatu)

@tree.command(name="musicgame_random", description="機種とレベルを選ぶと曲名を返してくれます", guild=discord.Object(id=YOUR_GUILT_ID))
async def mmusicgame_random(ctx:discord.Interaction, model:str, level:str):
    result = get_random_entry_from_db(model, level)
    
    if result:
        await ctx.response.send_message(f"ランセレの結果～ {result[1]}")
    else:
        await ctx.response.send_message("そんなもんねえよ")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=YOUR_GUILT_ID))
    print("ログインしました")

client.run(TOKEN)