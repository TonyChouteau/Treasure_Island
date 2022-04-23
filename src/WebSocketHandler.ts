/// <reference path="./WebSocketHandler.d.ts"/>
/// <reference path="./utils/utils.ts"/>

import type {UUID} from "./utils/utils";
import {create_UUID} from "./utils/utils";

const WebSocketHandler = function(this: any) {
    this.websocket = null;
    this.callback = null;

    this.messageHandlers = {};

    this.init();
    const handleWebSocket = () => {
        this.websocket.onerror = () => {
            this.init();
            handleWebSocket();
        };
        this.websocket.onopen = (data: Event) => {
            console.log(data)
            if (this.callback) {
                this.callback();
            }
        }
        this.websocket.onmessage = (event: MessageEvent) => {
            const eventJson: WebSocketEvent = JSON.parse(event.data);
            const handlers = this.messageHandlers[eventJson.type];
            if (handlers) {
                for (const id in handlers) {
                    this.messageHandlers[eventJson.type][id](eventJson.data);
                }
            }
        }
    }
    handleWebSocket();

} as WebSocketHandlerConstructor;

WebSocketHandler.prototype = {
    init: function() {
        this.websocket = new WebSocket("ws://localhost:8001/");
    },

    send: function(event: WebSocketEvent) {
        this.websocket.send(JSON.stringify(event));
    },

    on: function(name: string, callback: Function) {
        const uuid = create_UUID();
        if (!this.messageHandlers[name]) {
            this.messageHandlers[name] = {};
            this.messageHandlers[name][uuid] = callback;
        } else {
            this.messageHandlers[name][uuid] = callback;
        }
        return uuid;
    },

    off: function(name: string, uuid?: UUID) {
        if (uuid) {
            delete this.messageHandlers[name][uuid];
        } else {
            delete this.messageHandlers[name];
        }
    },

    whenReady: function(callback: Function) {
        if (this.websocket && this.websocket.readyState === WebSocket.OPEN) {
            callback();
        } else {
            this.callback = callback;
        }
    }
}

export default WebSocketHandler;