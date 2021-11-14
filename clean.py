from discord import message
from discord.ext import commands

bot = commands.Bot(command_prefix="~")

#청소
@bot.command(name="지워", pass_context=True)
async def _clear(ctx, *, amount=5):
    await ctx.send("잠깐만 ,,,")
    await ctx.channel.purge(limit=amount+2)
    await ctx.send("{} 개 만큼 지워써 !  " .format(amount))