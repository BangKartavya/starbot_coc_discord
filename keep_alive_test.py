from dashboard.dashboard import app
from threading import Thread

def keep_alive():   
    app.run()