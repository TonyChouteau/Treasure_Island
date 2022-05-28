interface Configuration {
    appContext: AppContext;

    selectableCharacters: ArrayLike<Selectable>;
    selected: number | void;
    players: Players;

    readyButton: JQuery;
    ready: boolean;

    displayCharacters(): void;
    handleReadyButton(): void;
    handleCharacterSelection(): void;
    handlePlayerList(): void;
}

interface ConfigurationConstructor {
    new (appContext: AppContext): Configuration;
    (): ConfigurationConstructor;
}

interface Player {
    name: string;
    pirate: void | string;
    full_name: void | string;
    ready: boolean;
}

type Players = ArrayLike<Player> & {
    filter(filter: Function): ArrayLike<Player>;
}

interface ReconnectData {
    selected: string;
    list: Players;
}