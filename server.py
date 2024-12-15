from flask import Flask

name = 'TestServer'

app = Flask(name)

@app.route('/')
def index():
    return { 'nickname': 'Miguel' }

app.run(debug=True, host="192.168.1.12")