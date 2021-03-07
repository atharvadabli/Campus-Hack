import discord
import datetime 
import time

color = 0xFF6500
key_features = {
    'temp' : 'Temperature(Celsius)',
    'feels_like' : 'Feels Like(Celsius)',
    'temp_min' : 'Minimum Temperature(Celsius)',
    'temp_max' : 'Maximum Temperature(Celsius)',
    'humidity' : 'Humidity(%)'
}
weath = {'description': 'Description','icon':'icon'}
key_features2 = {
    "day": 'Temperature(Celsius)',
    "min": 'Minimum Temperature(Celsius)',
    "max": 'Maximum Temperature(Celsius)',
    "night":'Night Temp.(C)',
    "eve": 'Evening Temp. (C)',
    "morn": 'Morning Temp. (C)'
}
key_features3={
    'event':'Event',
    'description':'Description of event:'
}
def f(date):
    dt = datetime.datetime(int(date[6]+date[7]+date[8]+date[9]),int(date[3]+date[4]),int(date[0]+date[1]),12,0)
    return int(time.mktime(dt.timetuple()))

def parse_data1(data):
    
    del data['pressure']
    return data
def parse_data2(data):
    del data['main']
    del data['id']
    
    return data


def weather_message(data1,data2,data3,aqi,location):
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather in {location}.',
        color=color
    )
    for key in data1:
        message.add_field(
            name=key_features[key],
            value=str(data1[key]),
            inline=False
        )
    
    message.add_field(
            name= "Visibility(metres)",
            value=str(data2),
            inline=False)
    
    
    
    for key in data3 :
        if key == 'description':
            message.add_field(
                name=weath[key],
                value=(data3[key]),
                inline=False
            )
        elif key == 'icon':
            ur = f'http://openweathermap.org/img/w/{data3[key]}.png'
            message.set_thumbnail(url= ur)
    
    message.add_field(
            name= "AQI",
            value=str(aqi[0]),
            inline=False
        ) 
    
    return message


def weather_message2(data5,location):
    location = location.title()
    message = discord.Embed(
        title=f' 8- Day Weather Forecast for {location}',
        description=f'Here is the forecasted weather for {location}.',
        color=color
    )
    for i in range(8):
        
        for key in data5[i]:
            if key == 'dt':
                from datetime import datetime
                t = data5[i][key]
                dt_obj = datetime.fromtimestamp(t).strftime('%d-%m-%y') 
                message.add_field(
                name='Date',
                value=(dt_obj),
                inline=True
            )
            
            

            elif key == 'temp':
                message.add_field(
                name='  Temperature  ',
                value=(data5[i][key]['day']),
                inline=True
            )
            
            elif key == 'weather':
                
                
                message.add_field(
                name='  Description',
                value=(data5[i][key][0]['description']),
                inline=True)
            
        # message.add_field(
        #         name='______________________',
        #         value= ,
        #         inline=False
        #     )    
    return message


def weather_message3(data7,date,location):
    
    location = location.title()
    message = discord.Embed(
        title=f'{location} Weather',
        description=f'Here is the weather forecast for {location} on {date}.',
        color=color
    )
    for key in data7['temp']:
        message.add_field(
            name=key_features2[key],
            value=str(data7['temp'][key]),
            inline=False
        )
    message.add_field(
            name= "Humidity",
            value=str(data7['humidity']),
            inline=False
    )
    message.add_field(
            name= "Description",
            value=str(data7['weather'][0]['description']),
            inline=False
    )
    ur = f'http://openweathermap.org/img/w/{data7["weather"][0]["icon"]}.png'
    message.set_thumbnail(url= ur)
    return message

def weather_message4(location,aqi):
    location = location.title()
    message = discord.Embed(
        title=f'{location} AQI',
        description=f'Here is the Air Quality Values in {location}.',
        color=color
    )
    message.add_field(
            name= "AQI",
            value=str(aqi[0]),
            inline=False
        )
    
    message.add_field(
            name= "PM2.5",
            value=str(aqi[2]),
            inline=False
        )
    message.add_field(
            name= "PM10",
            value=str(aqi[3]),
            inline=False
        )
    message.add_field(
            name= "AQI alert",
            value=str(aqi[1]),
            inline=False
        )
    
    return message
def weather_message5():
    message = discord.Embed(
        title='AQI levels',
        description='Here are the Air Quality Levels.',
        color=color
    )
    message.add_field(
            name= "0-50",
            value= 'Good',
            inline=False
        )
    
    message.add_field(
            name= "50-100",
            value="Moderate",
            inline=False
        )
    message.add_field(
            name= "101-150",
            value="Unhealthy for sensitive groups",
            inline=False
        )
    message.add_field(
            name= "150-200",
            value= "Unhealthy",
            inline=False
        )
    
    message.add_field(
            name= "201-300",
            value= "Very Unhealthy",
            inline=False
        )

    message.add_field(
            name= "301-500",
            value="Hazardous",
            inline=False
        )
    
    return message
def weather_message6(data8,location):
    location = location.title()
    if data8 == []:
        return discord.Embed(
        title='No Alerts',
        description=f'There are no weather alerts for {location}.',
        color=color
    )
    else:
        message = discord.Embed(
            title=f'{location} Weather Alerts',
            description=f'Here are the weather alerts in {location}.',
            color=color
        )
        message.add_field(
            name="Title",
            value= data8[0]['title'],
            color = color
        )
        message.add_field(
            name="Description",
            value=data8[0]['description'],
            color = color
        )
        message.add_field(
            name="Severity",
            value=data8[0]['severity'],
            color = color
        )
        

def bot_intro():
    message = discord.Embed(
        title='Mausam Bot',
        description='Hello! I am Mausam, a bot for all seasons. You can try any of these and tell me what to do !! Just write these commands and I am available for you !',
        color=color
    )
    message.add_field(
            name= "1.) mausam.city",
            value= "I will tell how's the weather right now at that city. Temperature, Humidity, Air Quality etc. ",
            inline=False
        )
    
    message.add_field(
            name= "2.) forecast8days.city",
            value=" will give a brief forecast of weather for next 8 days",
            inline=False
        )
    message.add_field(
            name= "3.) forecast.DD/MM/YYYYcity",
            value="will give a bit detailed weather forecast of given date. Don't forget the format!",
            inline=False
        )
    message.add_field(
            name= "4.) aqi.city",
            value= "will tell the quality of air around the city, the AQI level",
            inline=False
        )
    
    message.add_field(
            name= "5.) val.aqi",
            value= "will give the standard interpretation of AQI, so that you may know how healthy or unhealthy is the air.",
            inline=False
        ) 
    message.add_field(
            name= "6.)alerts.city",
            value= "will give the the weather alerts issued by competent authorities to make people aware of the various storms,severe snow fall etc.",
            inline=False
    )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
def error_message2(location,date):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location} on {date}.',
        color=color
    )
