# Campus-Hack 2021
## Our Bot- Meet our Weather Bot- Mausam!

## Getting Started:
###### We made a new bot through the discord developer portal, introduced it in our server and then wrote our code.

Our code is written in python.
To run our code, you must do the following installations:
## Installations:
######  pip install discord
######  pip install requests


######  pip install python-decouple
This install is used for hiding our API keys in python based code on github.

## How to run our code and make your own bot ?

Our code contains mainly following files:
main.py : This file runs the main send message & read message functions, Other files are embedded in this file. 

weather.py: This file contains the exact meassages which are to be sent, the main User- Interface is defined in this file. main.py file calls functions present in this file, to decide how exactly data/messages are to be sent.

To run this code and make your own bot, get your APIs from the respective websites, get the token of you discord bot, embed into the code.
Make a folder into your PC. Put all the files there. (You may put your api keys either into main.py with some modifications or by making a .env file) You have to run main.py to make Discord bot go online.


Once all the installations were done, we wrote the code and kept increasing the commands one by one and then finally debugged it and finalized it with the following commands.

## Commands:
######  mausam_bot.intro
######  mausam.location
######  forecast8days.location
######  forecast.datelocation
######  aqi.location 
######  val.aqi
######  alerts.location

Also, in this process, we took all the information needed for our bot from the following API's:

## API:
We took the following api's for our bot:
###### For news alerts: https://www.weatherbit.io/
###### For weather information: https://openweathermap.org/
###### For Aqi information: http://airpollutionapi.com/

