from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) # create an instance of the Flask class

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"


if __name__ == '__main__':
    serve(app,host="0.0.0.0", port=8000) # run the app in debug mode