# bot.py
import os
import re
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv
bot = commands.Bot(command_prefix="!")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



# TOKEN='MTA3MjE4NjE3NTYzMDA4NjE3Ng.GXMYHH.8-QBdZAw8FqZH8ehqARMalWL6Zc4-gPLx3dAOQ'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'test-umdbot':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye Byeee {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is how long your D is: {random.randrange(10)} Inches'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return
  
    # if 
    # 
    # message.author == client.user:
    #     return
    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hi')

async def dm_about_roles(member):
    print(f"DMing {member.name}...")

    await member.send(
        f"""Hi {member.name}, welcome to {member.guild.name}! 
        
Which of these languages do you use:
        
* CMSC (🐍)
* MATH (🕸️)
        
Reply to this message with one or more of the language names or emojis above so I can assign you the right roles on our server.
"""
    )

@bot.event
async def on_member_join(member):
    await dm_about_roles(member)

@bot.event
async def on_message(message):
    print("Saw a message...")
    
    if message.author == bot.user:
        return # prevent responding to self

    if isinstance(message.channel, discord.channel.DMChannel):
        await assign_roles(message)
        return
    # Respond to commands
    if message.content.startswith("!roles"):
        await dm_about_roles(message.author)
    elif message.content.startswith("!serverid"):
        await message.channel.send(message.channel.guild.id)

    
async def assign_roles(message):
    print("Assigning roles...")
    
    languages = set(re.findall("CMSC|MATH", message.content, re.IGNORECASE))
    
client.run(TOKEN)

