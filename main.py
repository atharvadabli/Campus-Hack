import discord
import requests
import json
from weather import *
from discord.ext.commands import Bot
token = 'ODE3Njc5NDc2OTM3NzE5ODI4.YENBWw.YXCPTCNB5__i02YI8SnFmiEcwFU'
api_key = '3dd56669bb9854ffe5fbacaa2818f7f9'
client = discord.Client()
command_prefix = 'w.'
command_prefix2 = 'aqi.'
command_prefix3 = 'val.aqi'
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='w.[location]'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='aqi.[location]'))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='val.aqi'))
@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, '')) >= 1:
            location = message.content.replace(command_prefix, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data1 = (json.loads(requests.get(url).content)['main'])
                data2 = (json.loads(requests.get(url).content)['visibility'])
                latitude = (json.loads(requests.get(url).content)['coord']['lat'])
                longitude = (json.loads(requests.get(url).content)['coord']['lon'])
                url2 = f'http://api.airpollutionapi.com/1.0/aqi?lat={latitude}&lon={longitude}&APPID=m17o2uh8c626ljgjuhj9kud0pp'
                alert = (json.loads(requests.get(url2).content)['data']['alert'])
                value = (json.loads(requests.get(url2).content)['data']['value'])
                pm25 = (json.loads(requests.get(url2).content)['data']['aqiParams'][1]['aqi'])
                pm10  = (json.loads(requests.get(url2).content)['data']['aqiParams'][2]['aqi'])
                aqi = [value, alert, pm25, pm10]
                await message.channel.send(embed=weather_message(data1,data2,location,aqi))
            except KeyError:
                await message.channel.send(embed=error_message(location))


    if message.author != client.user and message.content.startswith(command_prefix2):
        if len(message.content.replace(command_prefix2, '')) >= 1:
            location = message.content.replace(command_prefix2, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                latitude = (json.loads(requests.get(url).content)['coord']['lat'])
                longitude = (json.loads(requests.get(url).content)['coord']['lon'])
                url2 = f'http://api.airpollutionapi.com/1.0/aqi?lat={latitude}&lon={longitude}&APPID=m17o2uh8c626ljgjuhj9kud0pp'
                alert = (json.loads(requests.get(url2).content)['data']['alert'])
                value = (json.loads(requests.get(url2).content)['data']['value'])
                pm25 = (json.loads(requests.get(url2).content)['data']['aqiParams'][1]['aqi'])
                pm10  = (json.loads(requests.get(url2).content)['data']['aqiParams'][2]['aqi'])
                aqi = [value, alert, pm25, pm10]
                await message.channel.send(embed=weather_message2(location,aqi))
            except KeyError:
                await message.channel.send(embed=error_message(location))           
    

    if message.author != client.user and message.content.startswith(command_prefix3):
        
        await message.channel.send(embed = weather_message3())
        

client.run(token)
