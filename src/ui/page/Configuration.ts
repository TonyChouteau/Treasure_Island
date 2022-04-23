/// <reference path="./Configuration.d.ts"/>

import Selectable from "../components/selectable/Selectable";

const Configuration = function(websocketHandler: WebSocketHandler, game: Game) {
    this.websocketHandler = websocketHandler;
    this.game = game;

    this.selectableCharacters = [];
    this.selected = null;
    this.players = [];

    this.handleMapSelection();
    this.handleCharacterSelection();
    this.handlePlayerList();
    this.handleChat();
} as ConfigurationConstructor;

Configuration.prototype = {
    handleMapSelection: function() {
        // TODO
    },
    displayCharacters: function() {
        const characters = this.players.map((p: any) => p.pirate).filter((p: string) => p);
        this.selectableCharacters.forEach((selectable: Selectable) => {
            if (characters.includes(selectable.id) && !selectable.selected || (!selectable.selected && this.selected)) {
                selectable.handleDisable(true);
            } else if (!this.selected) {
                selectable.handleDisable(false);
            }
        });
    },
    handleCharacterSelection: function() {
        const characters = this.game.getCharacterList();
        const character_path = this.game.getCharacterPath();
        for (const id in characters) {
            let character = characters[id];
            this.selectableCharacters.push(new Selectable(".configuration_pirate", {
                backgroundImage: character_path + character.image_small,
                id: character.id,
                afterSelect: (selected: boolean) => {
                    if (selected) {
                        this.selected = id;
                    } else {
                        this.selected = null;
                    }
                    this.displayCharacters();
                    this.websocketHandler.send({
                        type: selected ? "select_pirate" : "unselect_player",
                        data: {
                            pirate_name: character.id
                        }
                    });
                },
                style: {
                    width: "20vw",
                    height: "20vw",
                    margin: "1vw"
                },
                footer: "",
            }))
        }

        this.websocketHandler.on("player_list", (data: Players) => {
            this.players = data;
            this.displayCharacters();
            this.handlePlayerList();
        });
        this.websocketHandler.on("reconnect_select", (data: ReconnectData) => {
            this.selectableCharacters.forEach((selectable: Selectable) => {
                if (selectable.id === data.selected) {
                    selectable.handleSelect(true);
                    this.selected = data.selected;
                }
            });
            this.players = data.list;
            this.displayCharacters();
            this.handlePlayerList();
        });
    },
    handlePlayerList: function() {
        $(".configuration_players").html(this.players.map((player: Player) => {
            return `
                <div class="player_line">
                    <div>
                        ${player.username}
                        ${player.full_name ? ("(" + player.full_name + ")") : ""}
                    </div>
                </div>
            `;
        }));
    },
    handleChat: function() {
    },
}

export default Configuration;