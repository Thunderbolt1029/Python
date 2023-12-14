import discord
from discord.ext import commands
from discord import Embed

client = commands.Bot(command_prefix = "zb!")
client.remove_command(name="help")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def help(ctx):
    embed = Embed(title="Server Status Help Commands", colour=0x99d9ea)
    
    fields = [("zb!help", "Displays the help window", True)]

    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed=embed)
        
@client.command()
async def status(ctx):
    await ctx.send(content="its going good")

client.run('ODA5MTU5MzUwOTExMzY5Mjk2.YCRCXg.sV7NQESUrhDwcVX2i5UTTelHSS8')
