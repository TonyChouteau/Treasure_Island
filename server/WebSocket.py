import asyncio
import json

import websockets

from server.Client import Client
from server.Routes import Routes


class WebSocket:

    def __init__(self):
        # Handle Routes
        self.routes = Routes()
        # Run Websocket
        asyncio.run(self.main())

    # Each client has a handler
    async def handler(self, websocket):
        client = Client(websocket)

        while True:
            try:
                # Wait for a new message from the client
                message = await websocket.recv()
            except websockets.ConnectionClosedError:
                # If client is disconnected
                self.routes.disconnect(client)
                break
            except websockets.ConnectionClosedOK:
                # If client is disconnected
                self.routes.disconnect(client)
                break

            # Get content from message
            message = json.loads(message)

            data_type = message.get("type")
            if data_type is None:
                continue

            # If message type exists and can be handled, handle it
            result = self.routes.handle(data_type, message.get("data"), client)

            if result is not True and result:
                for client in self.routes.game.clients:
                    await client.websocket.send(json.dumps(result))

    async def main(self):
        async with websockets.serve(self.handler, "", 8001):
            await asyncio.Future()  # run forever, wait for new connection
