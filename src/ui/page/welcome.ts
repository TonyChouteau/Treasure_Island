/// <reference path="../../WebSocketHandler.d.ts"/>
import Modal from "../components/modal/Modal";

function welcome(appContext: AppContext) {
    const welcome_modal = new Modal(".welcome", {
        size: 1,
        title: "Veuillez choisir un pseudo :",
        content: `
            <input type="text" class="player_username">
        `,
        footer: [{
            buttonType: Modal.OK,
            text: "Confirmer",
            callback: () => {
                const username = $(".player_username").val();

                appContext.username = username;
                const event: WebSocketEvent = {
                    type: "player_join",
                    data: {
                        username: username
                    }
                }
                appContext.websocketHandler.send(event)
            }
        }]
    });
    const welcome_player_handler_uuid = appContext.websocketHandler.on("player_list", (data: ArrayLike<Player>) => {
        appContext.game.setUserList(data);
        welcome_modal.close();

        $(".welcome").addClass("hidden");
        $(".configuration").removeClass("hidden");

        appContext.websocketHandler.off("player_list", welcome_player_handler_uuid);
    });
}

export default welcome;