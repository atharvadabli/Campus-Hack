import discord
import requests
import json
from weather import *
from discord.ext.commands import Bot
from decouple import config

token = config('token')
api_key = config('api_key')
api_key2 = config('api_key2')
api_key3 = config('api_key3')

client = discord.Client()

command_prefix1 = 'mausam.'
command_prefix2 = 'forecast8days.' 
command_prefix3 = 'forecast.'
command_prefix4 = 'aqi.'
command_prefix5 = 'val.aqi'
command_prefix6 = 'alerts.'
command_prefix7 = 'mausam_bot.intro'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='mausam.[location]'))
    
@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix1):
        if len(message.content.replace(command_prefix1, '')) >= 1:
            location = message.content.replace(command_prefix1, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data1 = parse_data1(json.loads(requests.get(url).content)['main'])
                data2 = (json.loads(requests.get(url).content)['visibility'])
                data3 = parse_data2(json.loads(requests.get(url).content)['weather'][0])
                
                coord = (json.loads(requests.get(url).content)['coord'])
                url2 = f'http://api.airpollutionapi.com/1.0/aqi?lat={coord["lat"]}&lon={coord["lon"]}&APPID={api_key2}'
                alert = (json.loads(requests.get(url2).content)['data']['alert'])
                value = (json.loads(requests.get(url2).content)['data']['value'])
                pm25 = (json.loads(requests.get(url2).content)['data']['aqiParams'][1]['aqi'])
                pm10  = (json.loads(requests.get(url2).content)['data']['aqiParams'][2]['aqi'])
                aqi = [value, alert, pm25, pm10]
                
                
                
                await message.channel.send(embed=weather_message(data1,data2,data3,aqi,location))
                
            except KeyError:
                await message.channel.send(embed=error_message(location))
    elif message.author != client.user and message.content.startswith(command_prefix2):
        if len(message.content.replace(command_prefix2, '')) >= 1:
            location = message.content.replace(command_prefix2, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric' 
            try:
                data4 = (json.loads(requests.get(url).content)['coord'])
                url3 = f'https://api.openweathermap.org/data/2.5/onecall?lat={data4["lat"]}&lon={data4["lon"]}&exclude=current,minutely,hourly,alerts&appid={api_key}&units=metric'
                data5 = (json.loads(requests.get(url3).content)['daily'])
                await message.channel.send(embed=weather_message2(data5,location))
            except KeyError:
                await message.channel.send(embed=error_message(location))
    elif message.author!=client.user and message.content.startswith(command_prefix3):
        if len(message.content.replace(command_prefix3, '')) >= 1:
                date=''
                inp=message.content.replace(command_prefix3,'')
                for i in range(len(message.content.replace(command_prefix3,''))):
                    if i==10:
                        break
                    else:
                        date=date+inp[i]
                location = ''
                for i in range(10,len(message.content.replace(command_prefix3,''))):
                    location=location+inp[i]
                    location.lower()
                url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
                try:
                    coord = (json.loads(requests.get(url).content)['coord'])
                    url4=f'https://api.openweathermap.org/data/2.5/onecall?lat={coord["lat"]}&lon={coord["lon"]}&appid={api_key}&units=metric'
                    data6 = (json.loads(requests.get(url4).content)['daily'])
                    for i in range(len(data6)):
                        if f(date)==data6[i]['dt']:
                            data7=data6[i]
                            await message.channel.send(embed=weather_message3(data7,date,location))
                except KeyError:
                    await message.channel.send(embed=error_message2(location,date))
    elif message.author != client.user and message.content.startswith(command_prefix4):
        if len(message.content.replace(command_prefix4, '')) >= 1:
            location = message.content.replace(command_prefix4, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                coord = (json.loads(requests.get(url).content)['coord'])
                url2 = f'http://api.airpollutionapi.com/1.0/aqi?lat={coord["lat"]}&lon={coord["lon"]}&APPID={api_key2}'
                alert = (json.loads(requests.get(url2).content)['data']['alert'])
                value = (json.loads(requests.get(url2).content)['data']['value'])
                pm25 = (json.loads(requests.get(url2).content)['data']['aqiParams'][1]['aqi'])
                pm10  = (json.loads(requests.get(url2).content)['data']['aqiParams'][2]['aqi'])
                aqi = [value, alert, pm25, pm10]
                await message.channel.send(embed=weather_message4(location,aqi))
            except KeyError:
                await message.channel.send(embed=error_message(location))    
    
    elif message.author != client.user and message.content.startswith(command_prefix6):
        if len(message.content.replace(command_prefix6, '')) >= 1:
            location = message.content.replace(command_prefix6, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                coord = (json.loads(requests.get(url).content)['coord']) 
                url5 = f'https://api.weatherbit.io/v2.0/alerts?lat={coord["lat"]}&lon={coord["lon"]}&key={api_key3}' 
                data8 = (json.loads(requests.get(url5).content)['alerts'])
                await message.channel.send(embed=weather_message6(data8,location))
            except KeyError:
                await message.channel.send(embed=error_message(location))   
    elif message.author != client.user and message.content.startswith(command_prefix5):
        await message.channel.send(embed = weather_message5()) 
    elif message.author != client.user and message.content.startswith(command_prefix7):
        await message.channel.send(embed = bot_intro())
        
client.run(token)
