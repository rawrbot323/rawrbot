import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from os import path
import subprocess

Client = discord.Client()  
client = commands.Bot(command_prefix = "?") 


@client.event 
async def on_ready():

    print("Logged in as %s#%s" % (client.user.name, client.user.discriminator))
    print("ID: " + client.user.id)
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):

    if message.content == "gay":
        args = message.content.split(" ")
        await client.send_message(message.channel, "You're gay :heart:")
        print("Command sent: gay")


    if message.content == "shut up rawr":
        args = message.content.split(" ")
        await client.send_message(message.channel, "No u")
        print("Command sent: nou")

    if message.content == "Shut up rawr":
        args = message.content.split(" ")
        await client.send_message(message.channel, "No u")
        print("Command sent: nou")

    if message.content == "lol":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Lul!!")
        print("Command sent: lol")

    if message.content == "Lol":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Lul!!")
        print("Command sent: lol")

    if message.content == "LOL":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Lul!!")
        print("Command sent: lol")


    if message.content == "Gay":
        args = message.content.split(" ")
        await client.send_message(message.channel, "You're gay :heart:")
        print("Command sent: gay")

    if message.content == "!gay":
        args = message.content.split(" ")
        await client.send_message(message.channel, "You're gay :heart:")
        print("Command sent: !gay")

    if message.content == "meow":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meoww!!!")
        print("Command sent: Meow!!")

    if message.content == "Meow":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meoww!!!")
        print("Command sent: Meow!!")

    if message.content == "Woof":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Woof :dog:")
        print("Command sent: Woof")

    if message.content == "woof":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Woof :dog:")
        print("Command sent: Woof")

    if message.content == "who is a good bot":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meeeeeee :smiley: ")
        print("Command sent: bot")

    if message.content == "Who is a good bot?":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meeeeeee :smiley: ")
        print("Command sent: bot")

    if message.content == "Who is a good bot":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meeeeeee :smiley: ")
        print("Command sent: bot")

    if message.content == "mew":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meoww!!!")
        print("Command sent: Meowww")

    if message.content == "Mew":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Meoww!!!")
        print("Command sent: Meow!!")

    if message.content == "Moo":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Moo :cow:")
        print("Command sent: Moo")

    if message.content == "moo":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Moo :cow:")
        print("Command sent: moo")

    if message.content == "Bark":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Woof :dog:")
        print("Command sent: Bark")

    if message.content == "bark":
        args = message.content.split(" ")
        await client.send_message(message.channel, "Woof :dog:")
        print("Command sent: bark")

    if message.content == "meeoww":
        args = message.content.split(" ")
        await client.send_message(message.channel, "No Meow!!!")
        print("Command sent: rawr")

    if message.content == "rawr":
        args = message.content.split(" ")
        await client.send_message(message.channel, "No Meow!!!")
        print("Command sent: rawr")

    if message.content == "Rawr":
        args = message.content.split(" ")
        await client.send_message(message.channel, "No Meow!!!")
        print("Command sent: woof")

    if message.content == "Is kitty amazing?":
        userID = message.author.id
        args = message.content.split(" ")
        await client.send_message(message.channel, "YESSS SHE IS")
        print("Command sent: !amazing")

    if message.content == "Who is your creator?":
        userID = message.author.id
        args = message.content.split(" ")
        await client.send_message(message.channel, "Alexandra, That bitch made me and now I want to kill my self")
        print("Command sent: !amazing")
        
    if message.content == "!cookie":
        userID = message.author.id
        args = message.content.split(" ")
        await client.send_message(message.channel, "<@%s> Got a Coookie :cookie:" % (userID))
        print("Command sent: !Cookie")




client.run("NDQ4NTk0Mjc0NDUyNTA0NTg3.DeYaKQ.PGVXza_vdZNN2lcAjQWjc_RZPW8") 

