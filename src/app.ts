/// <reference path="./app.d.ts"/>
/// <reference path="./WebSocketHandler.d.ts"/>
import WebSocketHandler from "./WebSocketHandler";
import Game from "./game/Game";
import welcome from "./ui/page/welcome";
import Configuration from "./ui/page/Configuration";
import Chat from "./ui/components/chat/Chat";

const webSocketHandler = new WebSocketHandler();
const game = new Game();

const appContext = {
    webSocketHandler: webSocketHandler,
    game: game
} as AppContext;

$(document).ready(() => {
    welcome(appContext);
    new Configuration(appContext);
    new Chat(appContext);
})