interface AppContext {
    webSocketHandler: WebSocketHandler;
    game: Game;
    username: void | string;
}

interface DomEvent extends Event {
    keyCode: number | void;
}