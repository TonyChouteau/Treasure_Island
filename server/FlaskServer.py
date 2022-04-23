from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def root():
    return send_from_directory("../public/", "index.html")

@app.route("/<path:path>")
def files(path):
    return send_from_directory("../public/", path)


if __name__ == "__main__":
    if os.path.isfile("./fullchain.pem"):
        app.run(host="vps.tonychouteau.fr", port=8002, debug=True, ssl_context=("./fullchain.pem", "./privkey.pem"))
    else:
        app.run()
