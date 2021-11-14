# Discode [ HING ] 
 디스코드 챗봇 [HING]은 신원중학교 친구들이 함께 만들었다.
 
 * 인사말 출력
   * ~힝
   ```python
   @bot.command()
   async def 힝(ctx):
       await ctx.send("힝 ~ ")
    ```
   * ~안녕
    ```python 
   @bot.command()
   async def 안녕(ctx):
       await ctx.send("하잉 ~")
    ```
   * 채팅 청소 : ~지워 (지울메세지수)
    ```python
   @bot.command(name="지워", pass_context=True)
   async def _clear(ctx, *, amount=5):
       await ctx.send("잠깐만 ,,,")
       await ctx.channel.purge(limit=amount+2)
       await ctx.send("{} 개 만큼 지워써 !  " .format(amount))
    ```
