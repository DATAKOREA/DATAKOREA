# -*- coding: utf-8 -*- 
import discord
import asyncio
import random 
import sys
import os
from send import Command
import TOKEN
from os import *

prefix = TOKEN.prefix

"""
봇 주인만 사용 가능한 비밀 명령어를 수록합니다.
"""


""" Function """
def restart_bot():
#    system('sudo reboot')
    python = sys.executable
    os.execl(python, python, * sys.argv)


""" Main """ 
class owner(Command):

    def __init__(self, *args, **kwargs):
        Command.__init__(self, *args, **kwargs)

        self.noticelist = ["봇-공지","봇_공지", "봇공지", "공지", "bot-notice", "bot_notice", "botnotice",  "notice", "bot-announcement", "botannouncment", "bot_announcement", "공지사항", "공지", "공지-사항", "공지입니다"]
        #self.noticelist = "botdevleopertestchannel"

    def search_notice_channel(self):

        allserver = []
        self.noticechannels = []
        for i in self.client.guilds:
            allserver.append(i)
        for b in allserver:
            for i in b.channels:
                if "bot-announcement" in i.name or "bot_announcement" in i.name or "봇-공지" in i.name or "봇_공지" in i.name:
                    self.noticechannels.append(i)
      
        for c in self.noticechannels:
            try:
                allserver.remove(c.guild)
            except:
                pass

        for b in allserver:
            for i in b.channels:
                if "bot-notice" in i.name or "bot_notice" in i.name:
                    self.noticechannels.append(i)
        for c in self.noticechannels:
            try:
                allserver.remove(c.guild)
            except:
                pass

        for b in allserver:
            for i in b.channels:
                if "notice" in i.name or "공지" in i.name:
                    self.noticechannels.append(i)
        for c in self.noticechannels:
            try:
                allserver.remove(c.guild)
            except:
                pass

        self.noserver = []
        for b in allserver:
            for i in b.channels:
                if "announcement" in i.name or "annoucement" in i.name:
                    self.noticechannels.append(i)

        for c in self.noticechannels:
            try:
                allserver.remove(c.guild)
            except:
                pass
        for a in allserver:
            self.noserver.append(a.name)

    async def on_message(self,message):
        if message.author.id == 355286685984227339:
            if message.content == prefix+"재시작":
                await message.channel.send("데이터코리아봇을 재시작합니다...")
                restart_bot()

            if message.content == prefix+"종료":
                await message.channel.send("데이터코리아봇을 종료합니다...")
                exit()

            if message.content.startswith(prefix+"강제초대"):
                a = message.content
                serverid = message.content.split(' ')[1]
                invite = self.client.get_channel(int(serverid))
            
                link = await invite.create_invite(max_uses=1, reason="자동 초대")
                
                await message.channel.send(link)


            if message.content.startswith(prefix+"공지"):
                contents = message.content[4:].lstrip()
                if contents == "" or contents is None:
                    await message.channel.send("내용을 입력하세요. 전송에 실패하였습니다.")
                else:
                    await message.channel.send("정말 전송합니까? (y/n)")
                    def usercheck(a):
                        return a.author == message.author

                    answer = await self.client.wait_for("message", check=usercheck, timeout=30)
                    answer = answer.content

                    if answer == "y":
                        self.search_notice_channel()
                        for i in self.noticechannels:
                            try:
                                await i.send(contents)
                            except:
                                pass
                        
                        await message.channel.send("전송 완료! 전송 하지 못한 서버들 : %s" %(self.noserver))
                    else:
                        await message.channel.send("전송을 취소합니다.")

            if message.content.startswith(prefix+'서버퇴장'):
                if message.content == prefix+'서버퇴장':
                    await message.channel.send('사용법: '+prefix+'서버퇴장 <서버아이디>')
                else:
                    a = message.content.split(' ')[1]
                    b = self.client.get_guild(int(a))
                    try:
                        await b.leave()
                        await message.channel.send('해당 서버에서 데이터코리아을 나가게 하였습니다.')
                    except Exception as error:
                        await message.channel.send('해당 서버에서 나가지 못했어요.```py\n{}\n```'.format(str(error)))
                


