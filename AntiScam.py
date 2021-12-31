import discord
import time
import pytz
from datetime import datetime
import pytz # $ pip install pytz
import locale
locale.setlocale(locale.LC_TIME, "es_ES")

message_content = ''
last_message = ''
last_message_content = ''
spam_counter = 0


async def AntiScam(message, bot, whitelist, muted_role, verified_role, logs_channel):
    global message_content, last_message, last_message_content, spam_counter
    message_content = f'{message.author.id}: {message.content}'
    message_content = message_content.replace("'", "`")
    mentions = message.raw_mentions
    # AntiScam-System
    if message_content == last_message_content and message.content != '' and message.author.id not in whitelist:
        spam_counter += 1
        await message.delete()
    else:
        last_message = message
        last_message_content = message_content
        spam_counter = 0

    if len(mentions) > 10 and message.author.id not in whitelist:
        await message.delete()
        spam_counter = 2

    if spam_counter > 1 and message.author.id not in whitelist:
        spam_counter = 0
        muted = discord.utils.get(message.author.guild.roles, name=muted_role)
        verified = discord.utils.get(message.author.guild.roles, name=verified_role)
        await last_message.delete()
        await message.author.add_roles(muted)
        await message.author.remove_roles(verified)
        channel = bot.get_channel(logs_channel)
        #await channel.send(f'USUARIO MUTEADO: {message_content}')

        la = pytz.timezone("Europe/Amsterdam")
        fmt =  "\n\n**Fecha:** %A, %d de %B de %Y" + "\n\n**Hora:** %H:%M:%S"
        now = datetime.now(la)
        #####
     



        embed = discord.Embed(title="info del usuario", description=f'**Usuario:** {message.author}' + "\n\n**ID: **"f"{message.author.id}"  + now.strftime(fmt) + "\n\n**Mensaje: **"f"{message.content}",color=discord.Colour.random())
        embed.set_thumbnail(url=f"{message.author.avatar_url}")
        
        await channel.send(embed=embed)
        
    
