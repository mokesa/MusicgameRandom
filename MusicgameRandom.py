import discord
from discord.ext import commands
from discord import app_commands

TOKEN = 'YOUR_TOKEN'
client = discord.client()
tree = discord.app_commands.CommandTree(client)

@tree.command(name="nya", description="にゃーん")
async def nya(ctx:discord.Intaraction):
    await ctx.response.send_message("にゃーん")

@client.event
async def on_ready():
    await tree.sync()
    print("ログインしました")

client.run(TOKEN)