#Importing libraries
import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

#"client" is the variable used to call upon events or commands in the program
my_secret = os.environ['token']
intents = discord.Intents.all() #Giving the bot access to external data
client = commands.Bot (command_prefix = '#',intents=intents) #setting prefix and intent access

#Ready messawaitge when bot turns on or is refreshed
#@client is the decorator 
@client.event
async def on_ready():
  print('Ready!')

#join message
@client.event
async def on_member_join(member):
    channel = client.get_channel(847221144250482688)
    await channel.send("Welcome")

#leave message
@client.event
async def on_member_remove(member):
    channel = client.get_channel(847221144250482688)
    await channel.send(f"{member} has left the server")

#staple ping command
@client.command()
async def ping(ctx):
  await ctx.send(f'{round(client.latency*1000)} ms')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'Reason for kick: {reason}')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'Banned: {member.mention}')

@client.command()
async def clear(ctx,amount:int):
  await ctx.channel.purge(limit=amount)

#Using token to connect the code to the app
client.run(my_secret)

