import asyncio
import discord

client = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NDU2Mjg1OTQxMzU5OTY4MjY3.DgIVWw.cslx4iXmNguXIzt59_2ZtUtAbDw"

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="서버컴 터짐 펑펑", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('아테나 명령어'): #만약 해당 메시지가 '아테나 명령어' 로 시작하는 경우에는
        await client.send_message(channel, '아직 없음,,,') #봇은 해당 채널에 '아직 없음,,,' 라고 말합니다.

    if    message.content.startswith('아테나 개발자'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '갓레나(SHANNON WILLIAMS)') #봇은 해당 채널에 '불렀음?' 라고 말합니다.

    if    message.content.startswith('아테나 뭐해'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '몰라') #봇은 해당 채널에 '불렀음?' 라고 말합니다.

    if    message.content.startswith('배그'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '나도 가치하장 ㅎㅎ') #봇은 해당 채널에 '불렀음?' 라고 말합니다.

    if    message.content.startswith('시발'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '욕하디마') #봇은 해당 채널에 '불렀음?' 라고 말합니다.

    if    message.content.startswith('ㅗ'): #만약 해당 메시지가 '아테나'로 시작하는 경우에는
        await client.send_message(channel, '욕은 나쁜거임 ') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
        
    if    message.content.startswith('지랄'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '욕은 나쁜거임 ') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
        
    if    message.content.startswith('씨발'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '욕은 나쁜거임  ') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
        
    if    message.content.startswith('凸'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '욕은 나쁜거임 ') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
        
    if    message.content.startswith('개새끼'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '보신탕') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
        
    if    message.content.startswith('힘들다'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '힘내') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
                
    if    message.content.startswith('좆까'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '의사양반임?') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
                
    if    message.content.startswith('병신'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '욕은 나쁜거 ㅇㅇ^^7') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
                        
    if    message.content.startswith('욱일기'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '간악한 쪽바리놈들') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
                        
    if    message.content.startswith('홍준표'): #만약 해당 메시지가 '아테나' 로 시작하는 경우에는
        await client.send_message(channel, '자유노땅당 원내대표이자 국민동네북 ') #봇은 해당 채널에 '불렀음?' 라고 말합니다.
        
    else: #위의 if에 해당되지 않는 경우
        #메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        await client.send_message(channel, "  ")

client.run(token)

