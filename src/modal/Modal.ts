/// <reference path="./Modal.d.ts"/>

const Modal = function(this: any, htmlNode: string, config: ModalConfig) {
    this.node = $(htmlNode);

    this.config = config;
    this.modal = null;
    this.initModal();

} as ModalConstructor;

Modal.OK = "OK";
Modal.CANCEL = "CANCEL";
Modal.DELETE = "DELETE";

Modal.prototype = {
    initModal: function() {
        const html: string = `
            <div class="modal_container">
                <div class="modal ${this.getSize()}">
                    <div class="modal_title">
                        ${this.config.title}
                    </div>
                    <div class="modal_content">
                        ${this.config.content}
                    </div>
                    <div class="modal_footer">
                    </div>
                </div>
            </div>
        `;

        this.modal = $(html);

        for (const id in this.config.footer) {
            const button: ModalButton = this.config.footer[id];
            $(".modal_footer", this.modal).append(`
                <div class="modal_button modal_button_${"" + button.buttonType}">
                    ${button.text}
                </div>
            `);
            $(`.modal_button_${button.buttonType}`, this.modal).on("click", (event: Event) => {
                button.callback();
            })
        }
        console.log("x")

        this.node.append(this.modal);
    },

    getSize: function() {
        if (!this.config.size) {
            return "";
        }
        switch(this.config.size) {
            case 1:
                return "modal_small";
            case 2:
                return "modal_medium";
            case 3:
                return "modal_large";
            default:
                return "";
        }
    },

    makeButton: function(button: ModalButton) {
        return `
            <div class="modal_button_${button}">
                ${button}
            </div>
        `;
    },

    close: function () {
        if (this.modal) {
            this.modal.remove();
        }
    }
};

export default Modal;