from server.web_socket import WebSocket
from utils.logger import Logger

Logger.debug_mode(True)

if __name__ == "__main__":
    websocket = WebSocket()
