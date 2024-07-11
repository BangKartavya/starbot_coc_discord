from dashboard.dashboard import app
from threading import Thread
import os
import uvicorn

def run():
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
    uvicorn.run(app,host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
