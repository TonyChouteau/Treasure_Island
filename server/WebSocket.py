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
                break

            # Get content from message
            event = json.loads(message)

            event_type = event.get("type")
            if event_type is None:
                break

            # If message type exists and can be handled, handle it
            self.route.handle(event_type, event)

    async def main(self):
        async with websockets.serve(self.handler, "", 8001):
            await asyncio.Future()  # run forever, wait for new connection
