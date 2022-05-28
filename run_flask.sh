export FLASK_APP=server/flask_server.py
flask run --host=0.0.0.0 --port=8002 --cert=cert.pem --key=privkey.pem
