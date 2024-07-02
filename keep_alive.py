# from flask import Flask,render_template
# from threading import Thread

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Alive"

# def run():
#     app.run(host='0.0.0.0',port=8080)

# def keep_alive():
#     t = Thread(target=run)
#     t.start()

from dashboard.dashboard import app
from threading import Thread

def keep_alive():   
    app.run(host = '0.0.0.0',port=5000)