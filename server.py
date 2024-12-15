from flask import Flask
from flask_cors import CORS

name = 'TestServer'

app = Flask(name)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/user')
def index():
    return { 'nickname': 'Nikita' }

app.run(debug=True)