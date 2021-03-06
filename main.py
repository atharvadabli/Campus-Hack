import discord
import requests
import json
from weather import *

token = 'ODE3NjQ1NjQxNDgzODEyODk1.YEMh2A.gOqlDXhEqM97PU5HkBoDJOSb65I'
api_key = '3dd56669bb9854ffe5fbacaa2818f7f9'
client = discord.Client()
command_prefix = 'w.'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='w.[location]'))

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, '')) >= 1:
            location = message.content.replace(command_prefix, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data1 = (json.loads(requests.get(url).content)['main'])
                data2 = (json.loads(requests.get(url).content)['visibility'])
                await message.channel.send(embed=weather_message(data1,data2,location))
                
            except KeyError:
                await message.channel.send(embed=error_message(location))

client.run(token)