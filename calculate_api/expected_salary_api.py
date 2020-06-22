from flask import Flask
app = Flask(__name__) # Active the flask application

@app.route('/hello_world')
def hello_world():
    return 'Hello, Tribe!'
# export FLASK_ENV=development
# to run in local server type flask run in the terminal