# Discode [ HING ] 
 <h5>디스코드 챗봇 [HING]은 지속되는 코로나19로 인해 오프라인 만남이 어려워진 친구들과 온라인에서 더욱 즐겁게 놀기 위해 제작되었습니다. ☺</h5>
 <h5>다양한 명령어를 사용해 간단한 대화를 주고받을 수 있습니다.</h5>
 <h5>명령어를 사용해 여러개의 채팅을 한번에 삭제할 수 있습니다.</h5>
 
 <hr>
 
 
 
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
 * 채팅 청소 
   * ~지워 (지울메세지수)
    ```python
   @bot.command(name="지워", pass_context=True)
   async def _clear(ctx, *, amount=5):
       await ctx.send("잠깐만 ,,,")
       await ctx.channel.purge(limit=amount+2)
       await ctx.send("{} 개 만큼 지워써 !  " .format(amount))
    ```


<hr>
<h5>만든사람들</th>
<h6>강윤 ㅣ kangyun0415@gmail.com</h6>
<h6>이해준 ㅣ ihae2660@gmali.com</h6>
<h6>곽채령 ㅣ 웅앙녕#5164</h6>
