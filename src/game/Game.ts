/// <reference path="./Game.d.ts"/>

const Game = function(this: any) {
    this.users = [];
} as GameConstructor;

Game.CHARACTERS_IMAGE_PATH = "./assets/character_avatar/";

Game.CHARACTERS = {
    jim: {
        id: "jim",
        name: "Jim Hawkins",
        image: "jim.jpg",
        image_small: "jim_small.jpg",
    },
    anne: {
        id: "anne",
        name: "Anne Bonny",
        image: "anne.jpg",
        image_small: "anne_small.jpg"
    },
    olivier: {
        id: "olivier",
        name: "Olivier Levasseur",
        image: "olivier.jpg",
        image_small: "olivier_small.jpg"
    },
    charlotte: {
        id: "charlotte",
        name: "Charlotte De Berry",
        image: "charlotte.jpg",
        image_small: "charlotte_small.jpg"
    },
    longjohn: {
        id: "longjohn",
        name: "Long John Silver",
        image: "longjohn.jpg",
        image_small: "longjohn_small.jpg"
    }
};

Game.prototype = {
    setUserList: function(userList: ArrayLike<Player>) {
        this.users = userList;
    },

    getCharacterList: function() {
        return Game.CHARACTERS;
    },

    getCharacterPath: function() {
        return Game.CHARACTERS_IMAGE_PATH;
    },
}

export default Game;