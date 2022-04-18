/// <reference path="./WebSocketHandler.d.ts"/>
import WebSocketHandler from "./WebSocketHandler";
import Game from "./game/Game";
import welcome from "./ui/page/welcome";
import Configuration from "./ui/page/Configuration";

const websocketHandler = new WebSocketHandler();
const game = new Game();

$(document).ready(() => {
    welcome(websocketHandler, game);
    new Configuration(websocketHandler, game);
})