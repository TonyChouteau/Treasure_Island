/// <reference path="./Configuration.d.ts"/>

import Selectable from "../components/selectable/Selectable";

const Configuration = function(websocketHandler: WebSocketHandler, game: Game) {
    this.websocketHandler = websocketHandler;
    this.game = game;

    this.selectableCharacters = [];

    this.handleMapSelection();
    this.handleCharacterSelection();
    this.handleChat();
    this.handlePlayerList();
} as ConfigurationConstructor;

Configuration.prototype = {
    handleMapSelection: function() {
        // TODO
    },
    handleCharacterSelection: function() {
        const characters = this.game.getCharacterList();
        const character_path = this.game.getCharacterPath();
        for (const id in characters) {
            let character = characters[id];
            this.selectableCharacters.push(new Selectable(".configuration_pirate", {
                backgroundImage: character_path + character.image_small,
                afterSelect: (selected: boolean) => {
                    this.selectableCharacters
                        .forEach((selectable: Selectable) => {
                            if (!selectable.selected) {
                                selectable.handleDisable(selected);
                            }
                        });
                    // TODO : Notify Websocket that a character is selected
                },
                style: {
                    margin: "20px"
                },
                footer: "",
            }))
        }
    },
    handleChat: function() {
        // TODO
    },
    handlePlayerList: function() {
        // TODO
    }
}

export default Configuration;