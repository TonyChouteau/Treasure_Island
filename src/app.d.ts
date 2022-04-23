interface AppContext {
    websocketHandler: WebSocketHandler;
    game: Game;
    chat: Chat;
    username: void | string;
}

interface DomEvent extends Event {
    keyCode: number | void;
}