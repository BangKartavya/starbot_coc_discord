from dashboard.dashboard import app
from mangum import Mangum
import os

def run():
    os.environ['AUTHLIB_INSECURE_TRANSPORT'] = '1'
    handler = Mangum(app)
