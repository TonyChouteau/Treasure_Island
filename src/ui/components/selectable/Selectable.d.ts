
interface Selectable {
    node: JQuery;
    config: SelectableConfig;
    selected: boolean;

    selectable: void | JQuery;
    makeSelectable(): void;
    handleSelect(selected?: boolean): void;
    handleDisable(disabled: boolean): void;
}

interface SelectableConstructor {
    new (node: string, config: SelectableConfig): Selectable;
    (): void;
}

interface SelectableConfig {
    id: string;
    backgroundImage: string;
    beforeSelect?: Function;
    afterSelect?: Function;
    style?: {
        width?: string;
        height?: string;
        margin?: string;
    };
    footer: string;
}