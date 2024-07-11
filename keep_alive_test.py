from dashboard.dashboard import app
import asyncio

def run():   
    app.run(host='0.0.0.0',port=8080)
