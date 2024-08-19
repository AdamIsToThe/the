
from discord import Client


sp = Client()



@sp.event
async def on_ready():

    with open('msgs.txt', 'a+') as fp:
        async for msg in (await sp.fetch_channel(1261436996044456037)).history(
            limit=9000000, oldest_first=True):
            print(msg.id)
            fp.write(msg.content + '\n')
            fp.write('\n'.join([x.proxy_url for x in msg.attachments]))

    



sp.run()
