
interface Chat {
    webSocketHandler: WebSocketHandler;
    node: void | JQuery;

    chatContainer: void | JQuery;
    messageContainer: void | JQuery;

    autoScrollEnabled: boolean;

    init(selector: string): void;
    setHandlers(): void;
    sendMessage(message: string): void;
    displayNewMessage(username: string, message: string): void;
    autoScroll(): void;
}

interface ChatConstructor {
    new (websocketHandler: WebSocketHandler): Chat;
    (): void;
}
interface IncomingMessage {
    sender: string;
    message: string;
}