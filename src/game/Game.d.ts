
interface Player {
    username: string;
    pirate: string | void;
}

interface Game {
    userList: ArrayLike<Player>;

    setUserList(userList: ArrayLike<Player>): void;
}

interface GameConstructor {
    new (): Game;
    (): void;

    CHARACTERS_IMAGE_PATH: string;
    CHARACTERS: Record<string, Pirate>;
}

interface Pirate {
    name: string;
    image: string;
    image_small: string;
}