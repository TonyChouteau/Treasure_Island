/// <reference path="./Chat.d.ts"/>

const Chat = function(this: any, appContext: AppContext) {
    this.webSocketHandler = appContext.webSocketHandler;
    this.node = null;

    this.chatContainer = null;
    this.messageContainer = null;

    this.autoScrollEnabled = true;

    this.init(".configuration_chat");
} as ChatConstructor;

Chat.prototype = {
    init: function(selector: string) {
        this.node = $(selector);

        const html = `
            <div class="chat_message_container">
                <div class="chat_content"></div>
            </div>
            <div class="chat_input_container">
                <input type="text" class="chat_input">
            </div>
        `;

        this.node.html(html);

        this.chatContainer = $(".chat_message_container", this.node);
        this.messageContainer = $(".chat_content", this.node);

        this.setHandlers();
    },

    setHandlers: function() {
        $(".chat_input", this.node).on("keypress", (e: DomEvent) => {
            if (e.keyCode === 13) {
                const messageInput = $(e.target);
                const message = messageInput.val();
                if (message !== "") {
                    this.sendMessage(message);
                    messageInput.val("");
                }
            }
        });
        this.chatContainer.on("scroll", () => {
            if (Math.abs(this.chatContainer.scrollTop() + this.chatContainer.height() - this.messageContainer.height()) < 5
                || this.chatContainer.height() > this.messageContainer.height()) {
                this.autoScrollEnabled = true;
            } else {
                this.autoScrollEnabled = false;
            }
            console.log(Math.abs(this.chatContainer.scrollTop() + this.chatContainer.height() - this.messageContainer.height()) < 10)
            console.log(this.autoScrollEnabled)
        })

        this.webSocketHandler.on("chat_message", (data: IncomingMessage) => {
            this.displayNewMessage(data.sender, data.message);
        });
    },

    sendMessage: function(message: string) {
        this.webSocketHandler.send({
            type: "chat_message",
            data: {
                new_message: message
            }
        });
    },

    displayNewMessage: function(username: string, message: string) {
        const gameMessage = username === "game";
        const html = `
            <div class="chat_message${gameMessage ? " game_message" : ""}">
                ${!gameMessage ? (username + " : ") : "" }${message.replace(/</g, "&lt;").replace(/>/g, "&gt;")}
            </div>
        `;
        $(".chat_content", this.node).append(html);
        this.autoScroll();
    },

    autoScroll: function() {
        if (this.autoScrollEnabled) {
            const chat_container = $(".chat_message_container", this.node);
            const chat_content = $(".chat_content", this.node);
            chat_container.scrollTop(chat_content.height());
        }
    },
}

export default Chat;