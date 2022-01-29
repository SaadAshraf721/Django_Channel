import asyncio

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class MySync(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected...", event)
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):

        print("Messaged Received...", event)
        print("Messaged", event['text'])
        for i in range(10):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):

        print("Websocket Disconnected...", event)
        raise StopConsumer()
