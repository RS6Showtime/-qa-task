import requests

def signup_user(username : str, password : str):

    protocol = "http://"
    directory = "signup"
    site = protocol + "localhost:8000/" + directory

    payload = {
        "username" : username,
        "password" : password
    }

    return requests.post(site, json=payload)

