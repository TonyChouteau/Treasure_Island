/// <reference path="./app.d.ts"/>
/// <reference path="./WebSocketHandler.d.ts"/>
import WebSocketHandler from "./WebSocketHandler";
import Game from "./game/Game";
import welcome from "./ui/page/welcome";
import Configuration from "./ui/page/Configuration";
import Chat from "./ui/components/chat/Chat";

const websocketHandler = new WebSocketHandler();
const game = new Game();
const chat = new Chat(websocketHandler);

const appContext = {
    websocketHandler: websocketHandler,
    game: game,
    chat: chat
} as AppContext;

$(document).ready(() => {
    welcome(appContext);
    new Configuration(appContext);
})