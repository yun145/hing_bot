import asyncio, discord
from logging import error
from discord import channel
from discord import message
from discord.ext import commands

bot = commands.Bot(command_prefix="~")

#로그인
@bot.event
async def on_ready():
	print("We have loggedd in as {0.user}".format(bot))

#명령어 정리
@bot.command()
async def 명령어(ctx):
    await ctx.send(embed = discord.Embed(title= "힝이가 할수있는고!", description = "인사 : 힝, 안녕\n청소 : 지워\n노래봇 사용법 : 재생 = 재생 + 노래제목\n \t\t  정지 = 노래멈춰\n \t\t 다시재생 = 다시틀어\n \t\t  노래끄기 = 노래꺼줘"))

#인사 ' 힝 '
@bot.command()
async def 힝(ctx):
    await ctx.send("힝 ~ ")

#인사 ' 안녕 '
@bot.command()
async def 안녕(ctx):
    await ctx.send("하잉 ~")

#없는 명령어 실행시
@bot.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound):
    	await ctx.send("힝 ~ 그런건 업써 ㅜ")


bot.run('') #토큰