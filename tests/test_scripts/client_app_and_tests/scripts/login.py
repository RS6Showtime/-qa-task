import requests

def login_user(username : str, password : str):

    protocol = "http://"
    directory = "login"
    site = protocol + "localhost:8000/" + directory

    payload = {
        "username" : username,
        "password" : password
    }

    return requests.post(site, json=payload)

