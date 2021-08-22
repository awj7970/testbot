from logging import fatal
import discord
import asyncio
import datetime
import random
import os

from discord import message
from discord import asset
from discord import activity
from discord import embeds

client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game("명령어")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content == "안녕":
        await message.channel.send(f"{message.author.name}님, 안녕하세요!                                                                           는 무슨")

    if message.content == "테스트":
        await message.channel.send("테스트 완료")

    if message.content == "크래딧":
        embed = discord.Embed(title="zzzzzzzzzz", color=0x00ff00)
        embed.set_footer(text="봇에 대한ㅁㄴㅇㄹ다.")
        await message.channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.content.startswith("정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("크래딧"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="[Creadit]", value=str("봇에 대한 설명입니다.") ,inline=True)
        embed.add_field(name="[개발자프로필]", value=str("----------->") ,inline=False)
        embed.add_field(name="[개발자]", value=str("B_ang") ,inline=False)
        embed.add_field(name="[개발환경]", value=str("Microsoft Visual Studio Code -- python") ,inline=False)
        embed.add_field(name="[E-mail]", value=str("awj7970@gmail.com -- gmail Mail") ,inline=False)
        embed.add_field(name="[Discord]", value=str("B_ang#2177") ,inline=False)
        embed.add_field(name="-----------------------------------------------------------", value=str("봇은 귀여와^^") ,inline=False)
        await message.channel.send(embed=embed)

    if message.content == "운세":
        ran = random.randint(1,3)
        if ran == 0:
            await message.channel.send(f"{message.author.name}님, 오해의 골이 생각보다 깊을 수 있습니다. 오늘은 넘기지 말고 먼저 풀어보세요.")
        if ran == 1:
            await message.channel.send(f"{message.author.name}님, 농담도 가려서 하는 것이 좋으니 말실수가 생기지 않도록 꼭 명심해야 합니다.")
        if ran == 2:
            await message.channel.send(f"{message.author.name}님, 뭐든 좋게 좋게 넘어가는 것이 낫지 않을까요? 작은 일은 작게 내버려 두세요.")
        if ran == 3:
            await message.channel.send(f"{message.author.name}님, 자신감있고 활기찬 모습이 좋으니 오늘은 큰 목소리로 어필해보길 바랍니다.")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
