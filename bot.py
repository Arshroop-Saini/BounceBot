import discord
import requests
from discord.ext import commands
import json
import random
import os
from dotenv import load_dotenv, find_dotenv


# API Requests
load_dotenv(find_dotenv())
Quote_URL = "https://zenquotes.io/api/random"

IMAGE_URL=f'https://picsum.photos/id/{random.randint(1,1000)}/info'
Joke_URL= 'https://v2.jokeapi.dev/joke/Any'

client = commands.Bot(command_prefix="$")

@client.command('quote')
async def quote(context):

   
    

    response = requests.get(Quote_URL)
    json_response = response.json()
    unique_quote = json_response[0]['q']
    author_name = json_response[0]['a']

    ress= requests.get(IMAGE_URL)
    json_ress= ress.json()
    width= json_ress['width']=1500
    height= json_ress['height']=1500
    image= json_ress["download_url"]=f'https://picsum.photos/id/{random.randint(1,1000)}/{width}/{height}'

    
    
    myEmbed= discord.Embed(title="Random Quote", description="Bounce!", color=0xff0000)
    myEmbed.add_field(name="Quote:",value=unique_quote,inline=False)
    myEmbed.add_field(name='Author',value=author_name,inline=False)
    myEmbed.set_thumbnail(url=image) 
    myEmbed.set_footer(text="Fetched using ZenQuotes and LoremPicsum API")
    
    await context.send(embed=myEmbed)

   
    

@client.command('version')
async def version(context):
        myEmbed= discord.Embed(title="Bot Version",description="Github repo: ", color=0x00ff00)
        myEmbed.add_field(name="The Bot is running on version",value="1.0.0",inline=False)
        myEmbed.add_field(name="Developer",value='Arshroop Singh',inline=False)
        myEmbed.set_footer(text="Thank you for using my me!") 

        await context.message.channel.send(embed=myEmbed)

@client.command('helpMe')
async def version(context):
    myEmbed= discord.Embed(title="Bot Commands",description="List of all the commands are as follows: ", color=0xff00ff)
    myEmbed.add_field(name="Prefix",value="s$",inline=False)
    myEmbed.add_field(name="version",value='Github repo, Developer, current version',inline=False)
    myEmbed.add_field(name="insprieMe",value='get a unique inspirational quote',inline=False)
    myEmbed.add_field(name="joke",value='get a joke form an array of categories',inline=False)
    myEmbed.set_footer(text="Don't forget to use the prefix $ before the commands") 

    await context.message.channel.send(embed=myEmbed)

@client.command('joke')
async def joke(context):
    
    res= requests.get(Joke_URL)
    res_json= res.json()
    type= res_json['type']
    category= res_json['category']
   
    
    if type== 'single':
        joke= res_json['joke']

        jEmbed= discord.Embed(title="Random Joke", description="Categories available: Minsc, Programming, Pun, Spooky, Christmas, Dark", color=0x00ffff)
        jEmbed.add_field(name="Category:",value=category,inline=False)
        jEmbed.add_field(name="Type:", value=type,inline=False)
        jEmbed.add_field(name='Joke:',value=joke,inline=False)
        jEmbed.set_footer(text="Fetched using JokeAPI")
        
        await context.send(embed=jEmbed)
    if type =='twopart':
        setup= res_json['setup']
        delivery= res_json['delivery']
        jEmbed= discord.Embed(title="Random Joke", description="Categories available: Minsc, Programming, Pun, Spooky, Christmas, Dark", color=0x00ffff)
        jEmbed.add_field(name="Category:",value=category,inline=False)
        jEmbed.add_field(name="Type:", value=type,inline=False)
        jEmbed.add_field(name='Setup:',value=setup,inline=False)
        jEmbed.add_field(name='Delivery:',value=delivery,inline=False)
        jEmbed.set_footer(text="Fetched using JokeAPI")
        
        await context.send(embed=jEmbed)
   
@client.command(name="command")
async def _command(ctx):
    
    await ctx.send('Please Enter A City Name')
    msg = await client.wait_for("message")
    message= msg.content.lower()
    await ctx.send(message)
    
  

    

@client.command('weather')
async def weather(context):
    # Asking for user input 
    await context.send('Please Enter A City Name')
    msg = await client.wait_for("message")
    message= msg.content.lower()
    api= os.environ.get('API')
    weather_url= f"https://api.openweathermap.org/data/2.5/weather?q={message}&appid={api}"
    



    res= requests.get(weather_url)
    res_json= res.json()

    # Displaying error if the user enter wrong city name
    cod= res_json['cod']
    if cod != 200:
        await context.send("Error")
    

    # city and country Name
    name= res_json['name']
    cname= res_json['sys']['country']

    # weather details
    main= res_json['weather'][0]['main']
    descrip= res_json['weather'][0]['description']

    # temperature details
    temp= res_json['main']['temp']
    min_temp= res_json['main']['temp_min']
    max_temp=res_json['main']['temp_max']
    pressure= res_json['main']['pressure']
    humidity= res_json['main']['humidity']

    # wind details
    speed= res_json['wind']['speed']

    # clouds
    clouds= res_json['clouds']['all']

    # sunrise and sunset
    sunrise= res_json['sys']['sunrise']
    sunset= res_json['sys']['sunset']

    # timezone
    timezone= res_json['timezone']
    
    # icon
    icon= res_json['weather'][0]['icon']
    icon_url= "http://openweathermap.org/img/w/" + icon + ".png"


    jEmbed= discord.Embed(title="Weather Condition", description="Weather Info available: weather description, clouds, sunrise and sunset, timezone, wind details, temperature details", color=0x6600ff)
    jEmbed.add_field(name="City:",value=name, inline=True)
    jEmbed.add_field(name="Country:", value=cname,inline=True)
    jEmbed.add_field(name='Timezone:',value=timezone,inline=True)

    jEmbed.add_field(name='Temperature:',value=temp,inline=True)
    jEmbed.add_field(name='Minimum',value=min_temp,inline=True)
    jEmbed.add_field(name='Maximum',value=max_temp,inline=True)
    
    jEmbed.add_field(name='Pressure:',value=pressure,inline=True)
    jEmbed.add_field(name='Humidity:',value=humidity,inline=True)
    jEmbed.add_field(name='Wind Speed:',value=speed,inline=True)

    jEmbed.add_field(name='Clouds:',value=clouds,inline=True)
    jEmbed.add_field(name='Sunrise:',value=sunrise,inline=True)
    jEmbed.add_field(name='Sunset:',value=sunset,inline=True)
    jEmbed.set_footer(text="Fetched using OpenWeather API")

    jEmbed.set_thumbnail(url=icon_url) 

    await context.send(embed=jEmbed)
    

@client.event
async def on_ready():
    #client will search for general channel and then print hello world.
    general_channel=client.get_channel(952228017986486312)
    await general_channel.send("Bounce!")
     


client.run(os.environ.get('TOKEN'))