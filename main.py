# -*- coding: utf-8 -*- 
import discord
import asyncio
import TOKEN
import importer
import datetime
from send import Command
from commands.background import *
from discord.ext import commands
import sys
import os
import time

prefix = TOKEN.prefix
loop = asyncio.get_event_loop()

try:
    os.system('cls')
except:
    os.system('clear')
print('\n\n봇을 시작합니다.')

class Bot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_command = []
        self.get_all_commands()
        self.loop = asyncio.get_event_loop()
        self.bg_task = self.loop.create_task(change_activity(self)) 
        print(self.load_command , "\n\n")
    def get_all_commands(self):
        for i in Command.commands:
            self.load_command.append(i(self))
    async def on_ready(self):
        print(self.user.name + "으로 봇이 로그인함.")
        print("=======")
        print("작동 시작!")
        print("\n\n")
    async def on_message(self, message):
        nowtime1 = datetime.datetime.now()
        try:
            servername = message.guild.name
            serverid = message.guild.id
            channelid = message.channel.id
            channelname = message.channel.name
        except:
            channelid = "DM이라 기록되지 않았습니다."
            channelname = "DM이라 기록되지 않았습니다."
            servername = "DM이라 기록되지 않았습니다."
            serverid = "DM이라 기록되지 않았습니다."
        if not message.attachments == []: # 보낸 메시지에 파일이 아무것도 없으면,
            attachedfile = message.attachments[0] # 첨부파일 정보를 받아온다. ( 정보는 다음과 같이 표시됨. [{"width": 1366, "url": "https://cdn.discordapp.com/attachments/397039361792802816/397726279668989963/unknown.png", "size": 222618, "proxy_url": "https://media.discordapp.net/attachments/397039361792802816/397726279668989963/unknown.png", "id": "397726279668989963", "height": 768, "filename": "unknown.png"}] )
            filelink = attachedfile.url # 저 데이터중 파일 url을 분석
            attach = filelink
        else:
            attach = "None"
        try:
            membersize = 0
            for i in message.guild.members:
                membersize = membersize + 1
            nobotsize = 0
            for i in message.guild.members:
                if i.bot == False:
                    nobotsize = nobotsize + 1
        except:
            membersize = 'DM이라 기록되지 않았습니다.'
            nobotsize = 'DM이라 기록되지 않았습니다.'
        print("%s + Message Helper\n       User: %s [ %s ]\n        Server: %s [ %s ]\n        ServerMember: %s [ notbot: %s ]\n       Channel: %s [ %s ]\n        Message: %s\n        File: %s\n        Embed: %s\n" %(nowtime1,message.author, message.author.id, servername, serverid, membersize, nobotsize, channelname, channelid, message.content,attach,message.embeds))
        if message.author.bot:
            return
        for i in self.load_command:
            self.loop.create_task(i._send(message))
client = Bot()
client.run(TOKEN.bot_token)
