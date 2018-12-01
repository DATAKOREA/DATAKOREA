# -*- coding: utf-8 -*- 
import discord
import asyncio
import TOKEN

"""
봇이 작동중에 사용할 백그라운드 태스크를 사용합니다.
"""

prefix = TOKEN.prefix

async def change_activity(self):
    await self.wait_until_ready()
    while not self.is_closed():

        number = 0
        user = 0

        for s in self.guilds:
            number = number + 1

            if not s.unavailable:
                user += s.member_count
        await self.change_presence(activity=discord.Game(name="%s개의 서버 / %s Servers"%(number,number)))
        await asyncio.sleep(20)
        await self.change_presence(activity=discord.Game(name="%s명의 유저 / %s Users"%(user, user)))
        await asyncio.sleep(20)
        await self.change_presence(activity=discord.Game(name="\'"+prefix+"도움\' 을 입력해보세요! | Try \'"+prefix+"cl\'"))
        await asyncio.sleep(20)

