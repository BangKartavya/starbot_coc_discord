import requests
from urllib.request import urlopen
import re as r
import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

email = os.getenv('email')
password = os.getenv('password')

def create_key(resp:requests.Response,name,desc,ip):
    try:
        resp.json()['error']
        print("There was an error during login,maybe the email and password are incorrect")
        return
    except KeyError:
        pass
    cookies = {
    'game-api-url': resp.json()['swaggerUrl'],
    'session': resp.cookies.get_dict()['session'],
    'game-api-token': resp.json()['temporaryAPIToken']
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://developer.clashofclans.com',
        'priority': 'u=1, i',
        'referer': 'https://developer.clashofclans.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'name': name,
        'description': desc,
        'cidrRanges': [ip],
        'scopes': None,
    }

    response = requests.post('https://developer.clashofclans.com/api/apikey/create', cookies=cookies, headers=headers, json=json_data)

    return response.json()['key']['key']

def login(email,password):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://developer.clashofclans.com',
        'priority': 'u=1, i',
        'referer': 'https://developer.clashofclans.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'email': email,
        'password': password,
    }
    response = requests.post('https://developer.clashofclans.com/api/login', headers=headers, json=json_data)
    return response

def load(resp:requests.Response):
    try:
        resp.json()['error']
        print("There was an error during login,maybe the email and password are incorrect")
        return
    except KeyError:
        pass
    cookies = {
    'game-api-url': resp.json()['swaggerUrl'],
    'session': resp.cookies.get_dict()['session'],
    'game-api-token': resp.json()['temporaryAPIToken']
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'origin': 'https://developer.clashofclans.com',
        'priority': 'u=1, i',
        'referer': 'https://developer.clashofclans.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {}

    response = requests.post('https://developer.clashofclans.com/api/account/load', cookies=cookies, headers=headers, json=json_data)
    
    return response

def logout(resp:requests.Response):
    try:
        resp.json()['error']
        print("There was an error during login,maybe the email and password are incorrect")
        return
    except KeyError:
        pass
    cookies = {
        'session' : resp.cookies.get_dict()['session']
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'origin': 'https://developer.clashofclans.com',
        'priority': 'u=1, i',
        'referer': 'https://developer.clashofclans.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {}

    response = requests.post('https://developer.clashofclans.com/api/logout', cookies=cookies, headers=headers, json=json_data)

def get_keys(resp:requests.Response):
    try:
        resp.json()['error']
        print("There was an error during login,maybe the email and password are incorrect")
        return
    except KeyError:
        pass
    cookies = {
        'game-api-url': resp.json()['swaggerUrl'],
        'session': resp.cookies.get_dict()['session'],
        'game-api-token': resp.json()['temporaryAPIToken']
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'origin': 'https://developer.clashofclans.com',
        'priority': 'u=1, i',
        'referer': 'https://developer.clashofclans.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {}

    # response = requests.get(url = 'https://developer.clashofclans.com/api/apikey/list',cookies=cookies,headers=headers,json=json_data)
    response = requests.post('https://developer.clashofclans.com/api/apikey/list', cookies=cookies, headers=headers, json=json_data)

    return response

def remove_keys(resp:requests.Response):
    try:
        resp.json()['error']
        print("There was an error during login,maybe the email and password are incorrect")
        return
    except KeyError:
        pass
    cookies = {
    'game-api-url': resp.json()['swaggerUrl'],
    'session': resp.cookies.get_dict()['session'],
    'game-api-token': resp.json()['temporaryAPIToken']
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://developer.clashofclans.com',
        'priority': 'u=1, i',
        'referer': 'https://developer.clashofclans.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    for i in get_keys(resp).json()['keys']:
        json_data = {
            'id': i['id'],
        }

        requests.post('https://developer.clashofclans.com/api/apikey/revoke', cookies=cookies, headers=headers, json=json_data)

def get_key_with_ip(resp:requests.Response,ip):
    keys = get_keys(resp).json()['keys']
    for i in keys:
        for j in i['cidrRanges']:
            if(j == ip):
                return i['key']

    return None 

if __name__ == "__main__":
    log = login(email,password)
    ip = load(log).json()['developer']['prevLoginIp']
    create_key(log,'Wow WOW WOOW','new day new key',ip)
    remove_keys(log)
    print(get_key_with_ip(log,ip))
        
    logout(log)
    print("Logged out successfully")

