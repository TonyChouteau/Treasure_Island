interface WebSocketHandler {
    websocket: WebSocket;

    init(): void;
    send(message: string): void;
    whenReady(callback: Function): void;
}

interface WebSocketHandlerConstructor {
    new (): WebSocketHandler;
    (): void;
}

interface Event {
}