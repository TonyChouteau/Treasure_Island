/// <reference path="./Configuration.d.ts"/>

import Selectable from "../components/selectable/Selectable";
import Button from "../components/button/Button";

const Configuration = function(appContext: AppContext) {
    this.webSocketHandler = appContext.webSocketHandler;
    this.game = appContext.game;

    this.selectableCharacters = [];
    this.selected = null;
    this.players = [];

    this.ready = false;

    this.handleReadyButton();
    this.handleCharacterSelection();
    this.handlePlayerList();
} as ConfigurationConstructor;

Configuration.prototype = {
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
    handleReadyButton: function() {
        this.readyButton = new Button(".configuration_start", {
            text: "Ready <span class='players'></span>",
            class: "button_ready",
            callback: () => {
                this.ready = !this.ready;
                if (this.ready) {
                    $(".button_ready").addClass("button_on");
                } else {
                    $(".button_ready").removeClass("button_on");
                }
                this.webSocketHandler.send({
                    type: "player_ready",
                    data: {
                        "ready": this.ready
                    }
                });
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
                    this.webSocketHandler.send({
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

        this.webSocketHandler.on("player_list", (data: Players) => {
            this.players = data;
            this.displayCharacters();
            this.handlePlayerList();

            const total = data.length;
            const ready = data.filter((p: Player) => p.ready).length;
            console.log(data);
            $(".players", this.readyButton.button).html(ready + "/" + total);
        });
        this.webSocketHandler.on("reconnect_select", (data: ReconnectData) => {
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
}

export default Configuration;