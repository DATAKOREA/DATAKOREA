# -*- coding: utf-8 -*- 
import discord
import datetime
import os
import random
from bs4 import BeautifulSoup
import sys 
import aiohttp
import asyncio
import requests 
import json 
import time


import TOKEN
from send import Command

prefix = TOKEN.prefix

"""
봇의 간단한 문답 기능을 수록합니다.
단, 간단하게 채팅으로 가능한 명령어는 이곳에 수록합니다. 
{100줄 이상 명령어 또는 특수 기능(게임 등)은 제외}
"""

# def restart_bot():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)

""" Function """
def htmltotext(html):
    soup = BeautifulSoup(html)
    text_parts = soup.findAll(text=True)
    return "".join(text_parts)

def right_check(a):
    try:
        if a is None or a == "":
            return "정보가 없습니다."

        else:
            return a

    except:
        return "정보를 찾을 수 없습니다."


def lxml_string(soup, tag):
    try:    
        find = soup.find(tag).string
        if find is None or find == "":
            return "정보가 존재하지 않음."
        else:
            return find
    except:
        return "정보 없음."


def checkpm10(n):
    try:
        n = int(n)
        if n >= 0 and n < 31:
            return "좋음"
        elif n >= 31 and n < 81:
            return "보통"
        elif n >= 80 and n < 151:
            return "`나쁨`"
        elif n >= 151:
            return "**`매우 나쁨`**" 

    except:
        return ""

def checkpm25(n):
    try:
        n = int(n)
        if n >= 0 and n < 16:
            return "좋음"
        elif n >= 16 and n < 36:
            return "보통"
        elif n >= 36 and n < 76:
            return "`나쁨`"
        elif n >= 76:
            return "**`매우 나쁨`**" 

    except:
        return ""

""" Main """

class chatting(Command):
    
    def __init__(self, *args, **kwargs):
        Command.__init__(self, *args, **kwargs)
        self.bot_start_time = datetime.datetime.now()
        
    async def on_message(self, message):
        if message.content.startswith(prefix+"업타임"):
            uptime = datetime.datetime.now() - self.bot_start_time
            # days = uptime.day
            # hours = uptime.hour
            # minitues = uptime.minute
            # seconds = uptime.second
            day = uptime.days
            day = str(day)

            uptime = str(uptime)
            uptime = uptime.split(":")

            hours = uptime[0]

            hours = hours.replace(" days,","일")
            hours = hours.replace(" day,","일")

            minitues = uptime[1]

            seconds = uptime[2]
            seconds = seconds.split(".")
            seconds = seconds[0]

            embed=discord.Embed(title="업타임", description="데이터코리아 봇이 동작한 시간은  %s시간 %s분 %s초 입니다." %(hours,minitues,seconds) , color=0x237ccd)

            await message.channel.send(embed=embed)

        if message.content.startswith(prefix+"id"):
            memid = message.author.id
            embed=discord.Embed(title="당신의 ID는", description=str(int(memid))+" "+ "입니다.",color=0xd8ef56)
            await message.channel.send(embed=embed)

        if message.content.startswith(prefix+"도움") or message.content.startswith(prefix+"commandlist") or message.content.startswith(prefix+"cl"):
            a = message.content
            a = a[5:]
            if a == "":
                embed=discord.Embed(title="📜 도움말", description="데이터코리아 봇의 사용을 도와줄 도움말입니다. 다음 명령어 그룹들을 참고하세요.", color=0x237ccd)
                embed.add_field(name=prefix+"도움 기능", value="데이터코리아 봇에 있는 기능에 대해 알려드립니다.", inline=True)
                embed.set_footer(text="도움 명령어에 없는 명령어가 있을 수 있습니다.")
                try:
                    await message.author.send(embed=embed)
                    await message.channel.send("DM으로 메시지를 보냈습니다. 확인하세요.")
                except:
                    embed=discord.Embed(title="⚠ 주의", description="DM 보내기에 실패하였습니다. 계정에서 DM 설정을 확인해주세요.",color=0xd8ef56)
                    await message.channel.send(embed=embed)
            elif a == "기능":
                embed=discord.Embed(title=" ", description="데이터코리아 봇에 있는 편리한 기능을 설명합니다.", color=0x237ccd)
                embed.add_field(name=prefix+"지진", value="지진 정보를 표시합니다.", inline=False)
                embed.add_field(name=prefix+"초대", value="데이터코리아 봇의 초대링크를 표시합니다.", inline=False)
                embed.add_field(name=prefix+"기상특보", value="기상특보 정보를 표시합니다.", inline=False)
                embed.add_field(name=prefix+"미세먼지", value="미세먼지 정보를 표시합니다.", inline=False)
                embed.add_field(name=prefix+"초미세먼지", value="초미세먼지 정보를 표시합니다.", inline=False)
                embed.add_field(name=prefix+"멜론차트", value="멜론 TOP10을 보여줍니다.", inline=False)
                embed.add_field(name=prefix+"가사검색", value="선택한 노래의 가사를 검색해줍니다. 가끔 다른 노래 가사가 들어갈수도 있으니 자세히 보기로 확인해보시는것도 좋아요!", inline=False)
                embed.add_field(name=prefix+"id", value="자신의 디스코드 ID를 보여줍니다.", inline=False)
                embed.add_field(name=prefix+"네이버실검", value="네이버 실시간 검색순위를 보여줍니다.", inline=False)
                embed.add_field(name="더 많은 기능은?", value="궁금증이나 도움 명령어에 수록되지 않은 명령어는 <@355286685984227339> 으로 친추후 DM해주세요!", inline=False)
                embed.set_footer(text="도움 명령어에 없는 명령어가 있을 수 있습니다.")
                try:
                    await message.author.send(embed=embed)
                except:
                    embed=discord.Embed(title="⚠ 주의", description="DM 보내기에 실패하였습니다. 계정에서 DM 설정을 확인해주세요.",color=0xd8ef56)
                    await message.channel.send(embed=embed)            
            else:
                embed=discord.Embed(title="⚠ 주의", description="일치하는 명령어가 없습니다. 도움 또는 commandlist (cl) 명령어를 사용해주세요.",color=0xd8ef56)
                await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"안녕") or message.content.startswith(prefix+"안냥") or message.content.startswith(prefix+"ㅎㅇ") or message.content.startswith(prefix+"gd") or message.content.startswith(prefix+"hello"):
            a = self.client.user.id
            bot_profile = self.client.get_user(a).avatar_url
            colorer = [0x000000,0xFFFFFF]
            colorers = random.choice(colorer)
            embed = discord.Embed(title="👋 반가워요.", description="점점 발전하고 있으니 잘 봐주세요!\n\n기능추가문의: (administrator@data-korea.com)" ,color=colorers)
            embed.set_thumbnail(url=bot_profile)
            await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"초대링크") or message.content.startswith(prefix+"초대") or message.content.startswith(prefix+"invite") or message.content.startswith(prefix+"join") or message.content.startswith(prefix+"초대링크내놔"):
            a = self.client.user.id
            bot_profile = self.client.get_user(a).avatar_url
            colorer = [0x000000,0xFFFFFF]
            colorers = random.choice(colorer)
            embed = discord.Embed(title="🙏초대해주시다니, 감사합니다!", description="초대 링크 : ('https://discordapp.com/api/oauth2/authorize?client_id=515144508027961365&permissions=8&scope=bot')" + "\n링크가 안먹히나요? TanzenT Lab. (administrator@data-korea.com) 에 연락을 주세요!" ,color=colorers)
            embed.set_thumbnail(url=bot_profile)
            await message.channel.send(embed=embed)

            
        if message.content.startswith(prefix+"핑"):
            nowasdf = datetime.datetime.now()
            await message.channel.trigger_typing()
            latertime = datetime.datetime.now()            
            ping = latertime - nowasdf

            asdf = str(int(ping.microseconds) / 1000)
            asdf = asdf.split(".")
            asdf = asdf[0]
            embed=discord.Embed(title="🏓 퐁! " + asdf+"ms", description=str(ping.microseconds) + "μs", color=0x237ccd)
            embed.set_footer(text="이 수치는 데이터코리아 봇이 메시지에 반응하는 속도입니다.")
            await  message.channel.send(embed=embed)
        if message.content.startswith(prefix+"퐁"):
            nowasdf = datetime.datetime.now()
            await message.channel.trigger_typing()
            latertime = datetime.datetime.now()            
            ping = latertime - nowasdf

            asdf = str(int(ping.microseconds) / 1000)
            asdf = asdf.split(".")
            asdf = asdf[0]
            embed=discord.Embed(title="🏓 핑! " + asdf+"ms", description=str(ping.microseconds) + "μs", color=0x237ccd)
            embed.set_footer(text="이 수치는 데이터코리아 봇이 메시지에 반응하는 속도입니다.")
            await message.channel.send(embed=embed)
        if message.content == (prefix+"지진"):
            async with aiohttp.ClientSession() as session:
                async with session.get("http://m.kma.go.kr/m/risk/risk_03.jsp#") as r:

                    c = await r.text()
                    soup = BeautifulSoup(c,"html.parser")
                    all = soup.find_all("div",{"id":"div_0"})
                    a = right_check(all[0].find_all("td",{"class":"tal pad2"})[0].text)
                    b = right_check(all[0].find_all("td",{"class":"tal pad2"})[1].text)
                    c = right_check(all[0].find_all("td",{"class":"tal pad2"})[2].text)
                    d = right_check(all[0].find_all("td",{"class":"tal pad2"})[3].text)
                    e = right_check(all[0].find_all("td",{"class":"tal pad2"})[4].text)
                    f = right_check(all[0].find_all("td",{"class":"tal pad2"})[5].text)
                    embed=discord.Embed(title="지진 정보", description=a,color=0x62bf42)
                    try:
                        img = all[0].find_all("img")[0]["src"]
                        img = "http://m.kma.go.kr" + img
                        if img is None: pass
                        else: embed.set_image(url=img)
                    except:
                        pass
                    embed.add_field(name="규모", value=b, inline=True)
                    embed.add_field(name="발생위치", value=c, inline=True)
                    embed.add_field(name="발생깊이", value=d, inline=True)
                    embed.add_field(name="진도", value=e, inline=True)
                    embed.add_field(name="참고사항", value=f, inline=True)
                    embed.set_footer(text="기상청")
                    await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"미세먼지"):
            async with aiohttp.ClientSession() as session:
                async with session.get("http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?serviceKey="+TOKEN.misaekey+"&numOfRows=1&pageSize=1&pageNo=1&startPage=1&itemCode=PM10&dataGubun=HOUR") as r:
                    c = await r.text()
                    
                    soup = BeautifulSoup(c,"lxml-xml")
                    datatime = lxml_string(soup, "dataTime")
                    seoul = lxml_string(soup, "seoul")
                    busan = lxml_string(soup, "busan")
                    daegu = lxml_string(soup, "daegu")
                    incheon = lxml_string(soup, "incheon")
                    gwangju = lxml_string(soup, "gwangju")
                    daejon = lxml_string(soup, "daejeon")
                    ulsan = lxml_string(soup, "ulsan")
                    gyeonggi = lxml_string(soup, "gyeonggi")
                    gangwon = lxml_string(soup, "gangwon")
                    chungbuk = lxml_string(soup, "chungbuk")
                    chungnam = lxml_string(soup, "chungnam")
                    jeonbuk = lxml_string(soup, "jeonbuk")
                    jeonnam = lxml_string(soup, "jeonnam")
                    gyeongbuk = lxml_string(soup, "gyeongbuk")
                    gyeongnam = lxml_string(soup, "gyeongnam")
                    jeju = lxml_string(soup, "jeju")
                    sejong = lxml_string(soup, "sejong")
                    sido = {"서울" : seoul, "부산" : busan, "대구":daegu, "인천":incheon, "광주":gwangju, "대전":daejon, "울산":ulsan, "경기":gyeonggi, "강원": gangwon, "충북": chungbuk, "충남":chungnam, "전북":jeonbuk, "전남" : jeonnam, "경북" : gyeongbuk, "경남" : gyeongnam, "제주":jeju, "세종": sejong}
                    embed=discord.Embed(title="💨 PM10 미세먼지 농도", description=datatime + " 기준", color=0x1dc73a )
                    embed.set_footer(text="에어코리아")
                    name = message.content[6:].lstrip()
                    if name == "":
                        for i in sido.keys():
                            embed.add_field(name=i, value="%s㎍/m³ | %s" %(sido[i], checkpm10(sido[i])), inline=True)
                        await message.channel.send(embed=embed)
                    else:
                        if name in sido.keys():
                            embed.add_field(name=name, value="%s㎍/m³ | %s" %(sido[name], checkpm10(sido[name])), inline=True)
                            await message.channel.send(embed=embed)
                        else:
                            embed=discord.Embed(title="⚠ 주의", description="지역 이름이 없습니다. 시·도별기준으로 불러오며, 도는 줄인 이름으로, 광역시는 `광역시` 글자를 제거해주세요.\n\n```ex) 경북, 경기, 서울, 광주...```",color=0xd8ef56)
                            await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"초미세먼지"):
            async with aiohttp.ClientSession() as session:
                async with session.get("http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?serviceKey="+TOKEN.misaekey+"&numOfRows=1&pageSize=1&pageNo=1&startPage=1&itemCode=PM25&dataGubun=HOUR") as r:
                    c = await r.text()
                    soup = BeautifulSoup(c,"lxml-xml")
                    datatime = lxml_string(soup, "dataTime")
                    seoul = lxml_string(soup, "seoul")
                    busan = lxml_string(soup, "busan")
                    daegu = lxml_string(soup, "daegu")
                    incheon = lxml_string(soup, "incheon")
                    gwangju = lxml_string(soup, "gwangju")
                    daejon = lxml_string(soup, "daejeon")
                    ulsan = lxml_string(soup, "ulsan")
                    gyeonggi = lxml_string(soup, "gyeonggi")
                    gangwon = lxml_string(soup, "gangwon")
                    chungbuk = lxml_string(soup, "chungbuk")
                    chungnam = lxml_string(soup, "chungnam")
                    jeonbuk = lxml_string(soup, "jeonbuk")
                    jeonnam = lxml_string(soup, "jeonnam")
                    gyeongbuk = lxml_string(soup, "gyeongbuk")
                    gyeongnam = lxml_string(soup, "gyeongnam")
                    jeju = lxml_string(soup, "jeju")
                    sejong = lxml_string(soup, "sejong")
                    sido = {"서울" : seoul, "부산" : busan, "대구":daegu, "인천":incheon, "광주":gwangju, "대전":daejon, "울산":ulsan, "경기":gyeonggi, "강원": gangwon, "충북": chungbuk, "충남":chungnam, "전북":jeonbuk, "전남" : jeonnam, "경북" : gyeongbuk, "경남" : gyeongnam, "제주":jeju, "세종": sejong}
                    embed=discord.Embed(title="💨 PM2.5 초미세먼지 농도", description=datatime + " 기준", color=0x1dc73a )
                    embed.set_footer(text="에어코리아")
                    name = message.content[7:].lstrip()
                    if name == "":
                        for i in sido.keys():
                            embed.add_field(name=i, value="%s㎍/㎥ | %s" %(sido[i], checkpm25(sido[i])), inline=True)
                        await message.channel.send(embed=embed)
                    else:
                        if name in sido.keys():
                            embed.add_field(name=name, value="%s㎍/㎥ | %s" %(sido[name], checkpm25(sido[name])), inline=True)
                            await message.channel.send(embed=embed)
                        else:
                            embed=discord.Embed(title="⚠ 주의", description="지역 이름이 없습니다. 시·도별기준으로 불러오며, 도는 줄인 이름으로, 광역시는 `광역시` 글자를 제거해주세요.\n\n```ex) 경북, 경기, 서울, 광주...```",color=0xd8ef56)
                            await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"가사검색"):   
            try:
                a = message.content[6:].lstrip()
                if a == "":
                    embed=discord.Embed(title="⚠ 주의", description="검색어가 없습니다.",color=0xd8ef56)
                    await message.channel.send(embed=embed)
                else:     
                    async with aiohttp.ClientSession() as session:
                        async with session.get("http://music.naver.com/search/search.nhn?query=" + a + "&target=track") as r:

                            c = await r.text()
                            soup = BeautifulSoup(c,"html.parser")
                            f = soup.find_all("a",{"title":"가사"})[0]["class"][1]
                            print(f)
                            f = f.split(",")
                            # print(f)
                            f = f[2]
                            f = f[2:]
                            load = "http://music.naver.com/lyric/index.nhn?trackId=" + f
                            async with aiohttp.ClientSession() as session:
                                async with session.get(load) as r:
                                    c = await r.text()
                                    soup = BeautifulSoup(c,"html.parser")
                                    f = soup.find("div",{"id":"lyricText"}).text
                                    f = f[:100]
                                    embed=discord.Embed(title="🎵 " + a + "에 대한 가사 검색", description="\n" + f +"...", color=0x237ccd)
                                    embed.add_field(name="자세히 보기", value=load, inline=False)

                                    await message.channel.send(embed=embed)
            except Exception as error:
                embed=discord.Embed(title="❌ 오류", description="오류가 발생하였습니다.\n%s",color=0xff0909)
                await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"이 서버는?") or message.content.startswith(prefix+"서버정보"):
            number = 0
            nonadminserver = []
            date = "%s (UTC)"% message.guild.created_at
            for i in message.guild.members:
                number = number + 1
            sunsunumber = 0
            for i in message.guild.members:
                if i.bot == False:
                    sunsunumber = sunsunumber + 1
            s = message.guild
            if s.get_member(self.client.user.id).guild_permissions.administrator == False:
                clear = "정리 대상 입니다."
            else:
                clear = "정리 대상이 아닙니다."
                try:
                    welcome = message.guild.system_channel.name
                    if welcome == "" or welcome is None:
                        welcome = "존재하지 않습니다."
                except:
                    welcome = "존재하지 않습니다."
                embed=discord.Embed(title="ℹ️ 서버 정보", description="이 서버에 대한 정보를 불러왔습니다.\n\n" , color=0x1dc73a)
                embed.add_field(name="이름", value=message.guild.name, inline=False)
                embed.add_field(name="서버 ID", value=message.guild.id, inline=True)
                embed.add_field(name="서버 인원", value=number, inline=True)
                embed.add_field(name="순수 서버 인원 (봇 제외)", value=sunsunumber, inline=False)
                embed.add_field(name="서버 생성일", value=date, inline=True)
                embed.add_field(name="서버 오너", value=message.guild.owner, inline=False)
                embed.add_field(name=prefix+"정리 대상", value=clear, inline=True)
                embed.add_field(name="웰컴 채널", value="#" + welcome, inline=False)
                embed.add_field(name="서버 위치", value=message.guild.region, inline=True)
                embed.set_thumbnail(url=message.guild.icon_url)
                await message.channel.send(embed=embed)
        if message.content.startswith(prefix+"멜론차트") or message.content.startswith(prefix+"맬론차트"):
            async with aiohttp.ClientSession() as session:

                async with session.get("https://music.cielsoft.me/api/getchart/melon") as r:

                    c = await r.text()
                    c = json.loads(c)
                    embed=discord.Embed(title="🎵 멜론 차트", description="멜론에서 TOP10 차트를 불러왔어요.",color=0x62bf42)
                    for i in range(15):
                        embed.add_field(name="TOP" + str(i+1),value=c[i]["title"] + " / " + c[i]["artist"])
                    await message.channel.send(embed=embed)

        if message.content == prefix+'네이버실검':
            async with aiohttp.ClientSession() as session:
                    async with session.get("http://naver.com") as r:
                        c = await r.text()
                # s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                        now = time.localtime()
                        now = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

                        soup = BeautifulSoup(c,"html.parser")
                        embed=discord.Embed(title="✅ 네이버 실시간 검색어", description=now + " 기준 네이버 실시간 검색어입니다. \n\n　", color=0x1dc73a)
                        number = 0
                        for i in soup.find_all("span",{"class":"ah_k"}):
                            try:
                                number = number + 1
                                print(i.text)
                                
                                embed.add_field(name=str(number) + "위", value=i.text, inline=False)
                                if number == 10:
                                    break

                            except:
                                pass
                        await message.channel.send(embed=embed)
