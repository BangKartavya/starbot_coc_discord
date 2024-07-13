import requests
import os
import dotenv
from clash_of_clans_wrapper.helper import Location

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

token = os.getenv('COC_API_KEY')


class Locations:
    def __init__(self):
        headers = {"Authorization" : f"Bearer {token}"}
        r = requests.get(url='https://api.clashofclans.com/v1/locations',headers=headers)
        self.j = r.json()

        self.locations = [Location(i) for i in self.j['items']]
