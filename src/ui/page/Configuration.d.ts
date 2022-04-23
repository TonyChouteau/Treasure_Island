interface Configuration {
    appContext: AppContext;

    selectableCharacters: ArrayLike<Selectable>;
    selected: number | void;
    players: Players;

    handleMapSelection(): void;
    handleCharacterSelection(): void;
    handleChat(): void;
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
}

type Players = ArrayLike<Player>

interface ReconnectData {
    selected: string;
    list: Players;
}