/// <reference path="./Game.d.ts"/>

const Game = function(this: any) {
    this.users = [];
} as GameConstructor;

Game.prototype = {
    setUserList: function(userList: ArrayLike<Player>) {
        this.users = userList;
    },
}

export default Game;