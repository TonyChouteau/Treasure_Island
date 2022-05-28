
interface Button {
    node: JQuery;
    config: ButtonConfig;
    button: JQuery;

    init(): void;
}

interface ButtonConstructor {
    new (selector: string, config: ButtonConfig): Button;
    (): void;
}

interface ButtonConfig {
    text: string;
    class?: string;
    callback: Function;
}