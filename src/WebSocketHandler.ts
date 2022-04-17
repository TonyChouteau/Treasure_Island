/// <reference path="./WebSocketHandler.d.ts"/>

const WebSocketHandler = function(this: any) {
    this.websocket = null;
    this.callback = null;

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
    }
    handleWebSocket();

} as WebSocketHandlerConstructor;

WebSocketHandler.prototype = {
    init: function() {
        this.websocket = new WebSocket("ws://localhost:8001/");
    },

    send: function(event: string) {
        this.websocket.send(event);
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