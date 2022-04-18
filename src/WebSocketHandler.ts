/// <reference path="./WebSocketHandler.d.ts"/>

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
            if (this.messageHandlers[eventJson.type]) {
                this.messageHandlers[eventJson.type](eventJson.data);
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
        this.messageHandlers[name] = callback;
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