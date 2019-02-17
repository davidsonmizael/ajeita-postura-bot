from config import *
import discord
import random
import os
import sys
import asyncio

def getVoiceList():
    voicelist = []
    for file in os.listdir(os.getcwd() + '/audios/'):
        if file.endswith('.mp3'):
            voicelist.append(file.split('.mp3')[0])
    return voicelist

def getRandom():
    voiceNo = random.choice(getVoiceList())
    return getVoice(voiceNo)

def getVoice(name):
    if name in getVoiceList():
        voice = os.path.join(os.getcwd(), 'audios/' + name + '.mp3')
        return voice
    return None

CMDLIST = { 'r': ['playVoice', 'Play random voice - Usage: .a r'],
            'v' : ['playVoice', 'Play voice by name - Usage: .a v <param> - Params: ' + ''.join(i + ' ' for i in getVoiceList()) ],
            'h': ['showHelp', 'Show this help - Usage: .a h']}

client = discord.Client()

async def playVoice(member, message=None, name=None):
    if name is None:
        voicePath = getRandom()
    else:
        voicePath = getVoice(name)
    
    if member.voice.voice_channel is None:
        if message is not None:
            msg = "You must be in a channel to call the bot."
            await client.send_message(message.channel, msg)
    else:
        if voicePath is not None:
            voice = await client.join_voice_channel(member.voice.voice_channel)
            player = voice.create_ffmpeg_player(voicePath)
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            await voice.disconnect()
        else:
            if message is not None:
                msg = "Invalid option."
                await client.send_message(message.channel, msg)

async def showHelp(member, message):
    msg = member.mention + "\n```\nCommand:\t\tHelp:\n---\n"
    for key, cmd in CMDLIST.items():
        msg = msg + key + "\t\t" + cmd[1] + "\n"
    msg = msg + "```"
    await client.send_message(message.channel, msg)

async def bg_task_alertposture():
    await client.wait_until_ready()
    while not client.is_closed:
        for channel in client.get_all_channels():
            if channel.voice_members:
                await playVoice(channel.voice_members[0])
        await asyncio.sleep(random.randint(INTERVALMIN,INTERVALMAX))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith(".a"):
        cmd = message.content.split(" ")
        if len(cmd) >= 2:
            if cmd[1] in CMDLIST:
                if len(cmd) == 3:
                    func = globals()[CMDLIST[cmd[1]][0]]
                    await func(message.author, message, cmd[2])
                else:
                    func = globals()[CMDLIST[cmd[1]][0]]
                    await func(message.author, message)
            else: 
                await showHelp(message.author, message)
        else:
            await showHelp(message.author, message)

@client.event
async def on_ready():
    print('Starting bot: {0}'.format(client.user.name))
    if ENABLEAUTOMESSAGE:
        print('The bot will visit all the channels arount every ' + str(int(((INTERVALMIN + INTERVALMAX)/2)/60)) + ' minutes.')
    print('URL to invite: https://discordapp.com/oauth2/authorize?client_id={0}&scope=bot&permissions=0'.format(client.user.id))
    print('------')

if ENABLEAUTOMESSAGE:
    client.loop.create_task(bg_task_alertposture())
client.run(TOKEN)