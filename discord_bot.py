import discord
import sys 
import  fibonacci
import equation
import requests
import json 

token = 'MTAzMTQ5MjgxNDI3OTgwNzAyNg.GSKZWW.TMXCEOpU9EeO1y9pmzcvhgJpBKp7C8RdM2_Oe4'
client = discord.Client(intents= discord.Intents.all())
prefix = "!"
def parseInt(str): 
    return int(str)

def getDogEmbeddedMessage(title, fieldName, color): 
    res = requests.get('https://dog.ceo/api/breed/shiba/images/random')
    imageUrl = res.json()['message']
    print(imageUrl)
    embedVar = discord.Embed(title= title, color=color)
    embedVar.set_image(url=imageUrl)
    return embedVar


def getCatEmbeddedMessage(title, fieldName, color): 
    res = requests.get('https://api.thecatapi.com/v1/images/search')
    imageUrl = res.json()[0]['url']
    embedVar = discord.Embed(title= title, color=color)
    embedVar.set_image(url=imageUrl)
    return embedVar


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content
    if(msg.startswith(prefix)):
        msg = msg.replace(prefix, '')
        if(msg.startswith("ping")):
            await message.channel.send("pong")

        elif(msg.startswith("fibo")):
            param = msg.split(" ")[1]
            print(param)
            await message.channel.send("the result is: " + str(fibonacci.Fibo(parseInt(param))))

        elif(msg.startswith("equation")):
            params = msg.split(" ")
            params.pop(0)
            await message.channel.send("the result is: " + str(equation.find_x(parseInt(params[0]), parseInt(params[1]), parseInt(params[2]))))

        elif(msg.startswith("dog")): 
            embedMsg = getDogEmbeddedMessage("Here is your dog image", "dog" , 3447003)
            await message.channel.send(embed=embedMsg)
        # elif(msg.startswith("cat")): 
        #     embedMsg = getCatEmbeddedMessage("Here is your cat image", "cat" , 3447003)
        #     await message.channel.send(embed=embedMsg)


client.run(token)