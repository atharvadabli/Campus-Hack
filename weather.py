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
    # del data['pressure']
    return data


def weather_message(data1,data2,location):
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
    return message


def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )