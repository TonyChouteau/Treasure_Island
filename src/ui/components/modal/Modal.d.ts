
interface Modal {
    node: JQuery;
    config: ModalConfig;
    modal: void | JQuery;

    initModal(): void;
    getSize(): string;
    makeButton(button: ModalButton): string;
    close(): void;
}

interface ModalConstructor {
    new (html_node: string, config: ModalConfig): Modal;
    (): void;

    OK: ModalButtonType;
    CANCEL: ModalButtonType;
    DELETE: ModalButtonType;
}

type ModalButtonType = string;
interface ModalButton {
    buttonType: ModalButtonType;
    text: string;
    callback: Function;
}

interface ModalConfig {
    size?: number;
    backgroudClose?: boolean;
    title: string;
    content: string;
    footer: ArrayLike<ModalButton>;
}
