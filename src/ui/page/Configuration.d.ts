
interface Configuration {
    websocketHandler: WebSocketHandler;
    game: Game;

    selectableCharacters: ArrayLike<Selectable>;
    selected: number | void;
    players: ArrayLike<{
        name: string;
        pirate: string;
    }>

    handleMapSelection(): void;
    handleCharacterSelection(): void;
    handleChat(): void;
    handlePlayerList(): void;
}

interface ConfigurationConstructor {
    new (websockethandler: WebSocketHandler, game: Game): Configuration;
    (): ConfigurationConstructor;
}