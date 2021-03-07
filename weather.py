import discord

color = 0xFF6500
key_features = {
    'temp' : 'Temperature(Celsius)',
    'feels_like' : 'Feels Like(Celsius)',
    'temp_min' : 'Minimum Temperature(Celsius)',
    'temp_max' : 'Maximum Temperature(Celsius)',
    'humidity' : 'humidity(%)',
    'pressure' : 'Pressure(hPa)'
}


def parse_data(data):
    # del data['humidity']
    # del data['pressure']S
    return data


def weather_message(data1,data2,location, aqi):
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
            inline=False
        )
    message.add_field(
            name= "AQI",
            value=str(aqi[0]),
            inline=False
        ) 
    return message


def weather_message2(location, aqi):
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


def weather_message3():
    message = discord.Embed(
        title='AQI levels',
        description='Here is the Air Quality Levels.',
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
def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
