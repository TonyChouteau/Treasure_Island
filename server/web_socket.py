import asyncio
import json
import os

import ssl
import websockets

from server.client import Client
from server.routes import Routes


class WebSocket:

    def __init__(self):
        # Handle Routes
        self.routes = Routes()
        # Run Websocket
        asyncio.run(self.main())

    def get_client(self, websocket):
        client = self.routes.get_client(websocket)
        if client is None:
            client = Client(websocket)
        return client

    async def handler(self, websocket):

        while True:
            try:
                # Wait for a new message from the client
                message = await websocket.recv()
            except websockets.WebSocketException:
                # If client is disconnected
                print("Disconnected")
                client = self.get_client(websocket)
                result = self.routes.disconnect(client)
                await self.response(result)
                break

            client = self.get_client(websocket)

            # Get content from message
            message = json.loads(message)

            data_type = message.get("type")
            if data_type is None:
                continue

            # If message type exists and can be handled, handle it
            result = self.routes.handle(data_type, message.get("data"), client)

            await self.response(result)

    async def response(self, result):
        if result is not True and result:
            for_client = result.get("for_client")
            if for_client:
                for client in for_client.keys():
                    await client.websocket.send(json.dumps(for_client.get(client)))
            broadcast = result.get("broadcast")
            if broadcast:
                for _client in self.routes.get_clients():
                    if _client.websocket is not None:
                        if _client.websocket.closed:
                            self.routes.disconnect(_client)
                        else:
                            await _client.websocket.send(json.dumps(broadcast))

    async def main(self):

        if os.path.isfile("./fullchain9.pem"):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            ssl_cert = "./fullchain9.pem"
            ssl_key = "./privkey9.pem"
            ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)
            async with websockets.serve(self.handler, "", 8001, ssl=ssl_context):
                await asyncio.Future()  # run forever, wait for new connection
        else:
            async with websockets.serve(self.handler, "", 8001):
                await asyncio.Future()  # run forever, wait for new connection
