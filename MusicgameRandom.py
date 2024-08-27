import discord
from discord.ext import commands
from discord import app_commands

TOKEN = 'YOUR_TOKEN'
intent = discord.Intents.all()
client = discord.Client(intents=intent)
tree = discord.app_commands.CommandTree(client)

@tree.command(name="nya", description="にゃーん")
async def nya(ctx:discord.Interaction):
    await ctx.response.send_message("にゃーん")

@client.event
async def on_ready():
    await tree.sync()
    print("ログインしました")

client.run(TOKEN)