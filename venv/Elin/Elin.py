# print("hello Elin!")

import discord
from konfig import Config

cc = Config("./../../config.ini")
token = cc.get_map("important_settings")['token']
# token = cc.get_map("important_settings")

# print(cc.as_args ())
# print(token)
# print(type(token))

elin = discord.Client()


prefix = ";"

@elin.event
async def on_ready():
    print('%s is ready!' % elin.user.name)
    # print()
    # print(client.user.id)
    print('------')

    pass

@elin.event
async def on_message(msg):

    if msg.author.id == elin.user.id: return

    if msg.content[0] != prefix:
        # print("dhgdhdh")
        return
    msg.content = msg.content[1:]

    print("message.content = ", msg.content)

    if msg.author.bot: return await msg.channel.send('봇은 싫어요! 저리 가세요!')

    if msg.content == "안녕!": await msg.channel.send('안녕하세요!')

    pass

elin.run(token)