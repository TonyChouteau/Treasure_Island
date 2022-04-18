
interface Configuration {
    websocketHandler: WebSocketHandler;
    game: Game;

    selectableCharacters: ArrayLike<Selectable>;

    handleMapSelection(): void;
    handleCharacterSelection(): void;
    handleChat(): void;
    handlePlayerList(): void;
}

interface ConfigurationConstructor {
    new (websockethandler: WebSocketHandler, game: Game): Configuration;
    (): ConfigurationConstructor;
}