import discord
from discord.ext import commands
import os

# Set up bot command prefix
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Event when bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Simple command
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! How can I assist you?")

# Command to check latency
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

# Run the bot using Replit secret key (store token in secrets)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
