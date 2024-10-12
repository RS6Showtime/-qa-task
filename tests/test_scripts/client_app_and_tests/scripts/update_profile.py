import requests

def update_user_profile(token: str, name : str = "abcabcabc", last_name : str = "abcabcabc"):

    protocol = "http://"
    directory = "profile"
    site = protocol + "localhost:8000/" + directory

    headers = {
        "Authorization": token
    }

    payload = {
        "name" : name,
        "last_name" : last_name
    }

    return requests.post(site, headers=headers, json=payload)

