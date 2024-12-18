from flask import Flask, app
import socketio
from flask_cors import CORS

flaskApp = Flask('TestApp')
cors = CORS(flaskApp)
socketServer = socketio.Server()

myApp = socketio.WSGIApp(socketServer, flaskApp)

@flaskApp.route('/')
def index():
    return 'Hello world!'

flaskApp.run(debug=True, port=5500)
myApp.run()