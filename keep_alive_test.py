from dashboard.dashboard import app
import os

def run():
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run(host='0.0.0.0',port=8080,debug=True)
