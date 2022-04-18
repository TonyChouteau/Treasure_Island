interface WebSocketHandler {
    websocket: void | WebSocket;
    callback: void | Function;

    messageHandlers: Record<string, Function>;

    init(): void;
    send(event: WebSocketEvent): void;
    on(name: string, callback: Function): void;
    whenReady(callback: Function): void;
}

interface WebSocketHandlerConstructor {
    new (): WebSocketHandler;
    (): void;
}

interface WebSocketEvent {
    type: string;
    data: any;
}