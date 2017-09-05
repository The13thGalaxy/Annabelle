#Annabelle v0.01
#Copyright Maya Pharis 2017

#GENERAL BOT STUFF

#Imports and Bot Command definition
import asyncio
import discord
import logging
import math
import os
import random
import sys
from discord import utils
from discord.ext.commands import Bot
logging.basicConfig(level = logging.INFO)

#Definition of BlitzKrieg's prefix.
my_bot = Bot(command_prefix = "&")


#Bot Startup
@my_bot.event
async def on_read():
    print("Annabelle initialized.")

#Commands

#Hello
@my_bot.command
async def hello():
    return await my_bot.say("Hey there. If you're looking for player info, use &players to see who I have available data for.")
    
#Player List
@my_bot.command
async def player():
    return await my_bot.say("As of this version, I currently have data for Galaxy.")


#PLAYERS

#Galaxy
@my_bot.command
async def Galaxy():
    return await my_bot.say("Player: **The13thGalaxy**\nMain Hero: **Widowmaker**\nSecondary Hero(es): **Genji and McCree**\nPocket Hero(es): **Reinhardt and Ana\nWorst Hero(es): **Lucio**\nFavorite Mode: **Payload**\nFavorite Map: **Watchpoint: Gibraltar**\nLeast Favorite Mode: **Control**\nLeast Favorite Map: **Oasis**")
    return await my_bot.say("Galaxy's Bio:\nDPS player, proficent in precision characters such as snipers. Typically flanks when not sniping.")

my_bot.run(token)