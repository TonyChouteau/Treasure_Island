/// <reference path="./WebSocketHandler.d.ts"/>
import WebSocketHandler from "./WebSocketHandler";
import Game from "./game/Game";
import welcome from "./hud/welcome";
import configuration from "./hud/configuration";

const websocketHandler = new WebSocketHandler();
const game = new Game();

$(document).ready(() => {
    welcome(websocketHandler, game);
    configuration(websocketHandler, game);
})