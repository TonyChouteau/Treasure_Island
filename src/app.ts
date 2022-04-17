/// <reference path="./WebSocketHandler.d.ts"/>
import WebSocketHandler from "./WebSocketHandler";

let websocketHandler = new WebSocketHandler();

$(document).ready(() => {
    websocketHandler.whenReady(() => {
        $(".hello").on("click", (e) => {
            const event = {
                type: "hello",
                data: [1, 2, 3]
            }
            websocketHandler.send(JSON.stringify(event));
        });
        $(".test").on("click", () => {
            const event = {
                type: "test",
                data: {
                    a: 1,
                    b: 2,
                    c: 3
                }
            }
            websocketHandler.send(JSON.stringify(event));
        });
    })
})