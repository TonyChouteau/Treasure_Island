let websocket_test = new WebSocket("ws://localhost:8001/");

$(document).ready(() => {
    $(".hello").on("click", () => {
        const event = {
            type: "hello",
            data: [1, 2, 3]
        }
        websocket_test.send(JSON.stringify(event));
    })
    $(".test").on("click", () => {
        const event = {
            type: "test",
            data: {
                a: 1,
                b: 2,
                c: 3
            }
        }
        websocket_test.send(JSON.stringify(event));
    })
})

websocket_test.addEventListener("open", (data) => {
    console.log(data)
})