# Okara Bot

import discord
import asyncio
import random

from discord.ext import commands

Bot = commands.Bot(description="Okara The Bot", command_prefix="!")

@Bot.event
async def on_ready():
    print("Okara is ready for the mission")


@Bot.command(pass_context=True)
async def Hi(context):
  possibleRes = ["Hello","Yo","Hi","Aay Lmao"]
  await Bot.say(random.choice(possibleRes) + ", " + context.message.author.mention + ":wave:")
  await Bot.say("Hope you are doing good")

@Bot.command(pass_context=True)
async def Bestfusion(ctx):
    await Bot.say("Kefla, No Doubt")

@Bot.command(pass_context=True)
async def UseUI(ctx):
    await Bot.say("Sorry, I think to much for that to happen")

@Bot.command(pass_context=True)
async def UseSSJ(ctx):
    await Bot.say("Lets get this going")
    await Bot.say('http://imgur.com/gallery/hB0Zuw7.png' .format(ctx))

@Bot.command(pass_context=True)
async def LetsBeFriends(ctx):
    await Bot.say("Sure thing but mess with me and you die")

@Bot.command(pass_context=True)
async def FightMe(ctx):
    await Bot.say("You sure about that ?")
    await Bot.say("I'm pretty sure I'll kick your ass")
    await Bot.say("Server:" + ctx.message.author.mention + "is badly damaged")

@Bot.command(pass_context=True)
async def WanaRP(ctx):
    await Bot.say("F**k. Off.")

@Bot.command(pass_context=True)
async def PlaySong(ctx):
    await Bot.say("I got some good shit right here!")
    await Bot.

Bot.run("NDQ3MjgwNDkxMDYyNzU1MzM4.DeFUDg.EnGEiGGJ5cEgyl4Ng9szDzM9JHQ")