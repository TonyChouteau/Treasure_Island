import asyncio
import json

import websockets

from server.Route import Route


class WebSocket:

    def __init__(self):
        # Handle Routes
        self.route = Route()
        # Run Websocket
        asyncio.run(self.main())

    # Each client has an handler
    async def handler(self, websocket):
        while True:
            try:
                # Wait for a new message from the client
                message = await websocket.recv()
            except websockets.ConnectionClosedOK:
                # If client is disconnected
                self.route.disconnect(websocket)
                break

            # Get content from message
            data = json.loads(message)

            data_type = data.get("type")
            if data_type is None:
                continue

            # If message type exists and can be handled, handle it
            self.route.handle(data_type, data, websocket)

    async def main(self):
        async with websockets.serve(self.handler, "", 8001):
            await asyncio.Future()  # run forever, wait for new connection