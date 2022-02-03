from email.mime import image
import discord
import requests
import io
import aiohttp

from discord.ext import commands
from yarl import URL


client = discord.Client()


@client.event
async def on_ready():
    print("Le bot est prêt")


@client.event
async def on_message(message):
    if message.content.startswith("/cat"):
        # Permet de récupérer un lien d'image de chat à partir d'une API :
        reponse = requests.get("https://api.thecatapi.com/v1/images/search")
        reponse = reponse.text
        indexStartUrl = reponse.find("url")
        indexEndUrl = reponse.find(".jpg")
        url = reponse[indexStartUrl+6 : indexEndUrl+4]
        
        # Renvoie l'image sous forme de message dans le serveur discord :
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await message.channel.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await message.channel.send(file=discord.File(data, 'cool_image.png'))


client.run("OTM2NzM1NTIyMjg0NTIzNTgy.YfRg8A._13axNvzL3osxh0v9JJmllI7oSE")