/// <reference path="./Selectable.d.ts"/>

const Selectable = function(this: any, node: string, config: SelectableConfig) {
    this.node = $(node);
    this.config = config;
    this.id = config.id;

    this.disabled = false;
    this.selected = false;

    this.selectable = null;
    this.makeSelectable();
} as SelectableConstructor;

Selectable.prototype = {
    makeSelectable: function() {
        let html = `
            <div class="selectable" style="${this.makeStyle()}">
                <div class="selectable_background" style="background-image: url(${this.config.backgroundImage})"></div>
            </div>
        `;

        this.selectable = $(html);

        $(".selectable_background", this.selectable).on("click", () => {
            if (!this.disabled) {
                let canceled = false;
                if (this.config.beforeSelect) {
                    canceled = this.config.beforeSelect(this.selected) === false;
                }
                if (!canceled) {
                    this.handleSelect();
                    if (this.config.afterSelect) {
                        this.config.afterSelect(this.selected);
                    }
                }
            }
        });

        this.node.append(this.selectable);
    },

    makeStyle: function() {
        const styleConfig = this.config.style;
        let styles = [];
        if (styleConfig) {
            if (styleConfig.width) {
                styles.push("width: " + styleConfig.width);
            } else {
                styles.push("flex-grow: 1");
                styles.push("width-max: ");
            }
            if (styleConfig.height) {
                styles.push("height: " + styleConfig.height);
            }
            if (styleConfig.padding) {
                styles.push("padding: " + styleConfig.padding);
            }
            if (styleConfig.margin) {
                styles.push("margin: " + styleConfig.margin);
            }
        } else {
            styles.push("flex-grow: 1");
        }

        return styles.join(";");
    },

    handleSelect: function(selected?: boolean) {
        if (!this.disabled) {
            if (selected !== undefined) {
                this.selected = selected;
            } else {
                this.selected = !this.selected;
            }
            if (this.selected) {
                $(".selectable_background", this.selectable).addClass("selectable_zoom");
            } else{
                $(".selectable_background", this.selectable).removeClass("selectable_zoom");
            }
        }
    },

    handleDisable: function(disabled: boolean) {
        this.disabled = disabled;
        if (this.disabled) {
            $(".selectable_background", this.selectable).addClass("disabled");
        } else {
            $(".selectable_background", this.selectable).removeClass("disabled");
        }
    }
};

export default Selectable;