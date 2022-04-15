import asyncio
import json

import websockets

from server.Route import Route


class WebSocket:

    def __init__(self):
        self.route = Route()

        asyncio.run(self.main())

    async def handler(self, websocket):
        while True:
            try:
                message = await websocket.recv()
            except websockets.ConnectionClosedOK:
                break

            event = json.loads(message)

            event_type = event.get("type")
            if event_type is None:
                break

            self.route.handle(event_type, event)

    async def main(self):
        async with websockets.serve(self.handler, "", 8001):
            await asyncio.Future()  # run forever
