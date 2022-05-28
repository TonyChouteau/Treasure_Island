/// <reference path="./Button.d.ts"/>

const Button = function(this: any, selector: string, config: ButtonConfig) {
    this.node = $(selector);
    this.config = config;

    this.init();
} as ButtonConstructor;

Button.prototype = {
    init: function() {
        const button_class = this.config.class;
        let html = `
            <div class="button${button_class ? (" " + button_class) : ""}">
                ${this.config.text}
            </div>
        `;
        this.button = $(html);

        this.button.on("click", this.config.callback);

        this.node.append(this.button);
    }
};

export default Button;