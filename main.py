import asyncio
import concurrent
import sys
import threading
import time

import discord

import nhentai

client = discord.Client()

import concurrent.futures


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if str.startswith(message.content, "&dt"):
        dog = 1
        ass = 0
        list = []
        lista = []
        string = ""
        numa = int(str.split(message.content, "&dt")[1])
        if (numa > 30):
            await message.channel.send("Your number of doujin's randomized need to be 30 or less.")
        else:
            num = (str(numa))
            mess = "Awaiting your requested " + num + " doujin's from https://nhentai.net" + " excluding every non execptable doujin that the 1880's would shame you for" + "\n this could take from " + num + " seconds to " + num + " minutes please wait...."
            await message.channel.send(mess)
            while dog:
                if (ass >= numa):
                    dog = 0
                else:
                    ass = ass + 1
                    print("speed")
                    balls = 1
                    ballsa = 1
                    rat = 0
                    doujina = None
                    while balls:
                        try:
                            doujin = nhentai.get_doujin(nhentai.get_random_id())
                            tags = doujin.tags
                            if "vore" in str(tags) or "anal" in str(tags) or "bisexual" in str(
                                    tags) or "shotacon" in str(tags) or "tomgirl" in str(
                                    tags) or "crossdressing" in str(tags) or "gender bender" in str(
                                    tags) or "bdsm" in str(tags) or "fart" in str(tags) or "vomit" in str(
                                    tags) or "scat" in str(tags) or "urination" in str(tags) in str(
                                    tags) or "gore" in str(tags) or "pegging" in str(tags) or "dickgirl on male" in str(
                                    tags) or "gag" in str(tags) or "bondage" in str(tags) or "yaoi" in str(
                                    tags) or "lolicon" in str(
                                    tags) or "males only" in str(tags):
                                rat = 1
                            if rat == 0:
                                balls = 0
                                doujina = doujin
                        except:
                            print("Unexpected error:", sys.exc_info()[0])
                            balls = 0
                            doujina = doujin
                            ballsa = 0
                            ass = ass-1
                            print("Pushed request to " + str(numa))

                    if (ballsa == 1):
                        response = doujina.url

                        list.append("Number:" + str(ass) + "\n Link: " + str(response))
                        lista.append(doujina)
                        print(response)

       ##     for x in (list):
       ##         if string == "":
       ####             string = x
        ##        else:
        ##            string = string + "\n" + x
         ##   await message.channel.send(string)


            for x in lista:
                e = discord.Embed()
                tagss = []
                titles = []
                for xz in x.tags:
                    if (tags == []):
                        tagss.append(str(xz.name))
                    else:
                        tagss.append(" " + str(xz.name))
                for xz in x.titles:
                    if (titles == []):
                        titles.append(str(xz))
                    else:
                        titles.append(" " + str(xz))
                e.set_image(url=x.cover)
                e.add_field(name="NAME",value=x.titles, inline=True)
                e.add_field(name="TAGS",value=tagss, inline=False)
                e.add_field(name="URL",value=x.url, inline=False)
                await message.channel.send(embed=e)





yourtoken = "000000000"
client.run(yourtoken)
