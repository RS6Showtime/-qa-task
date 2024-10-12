import requests

def view_user_profile(token: str):

    protocol = "http://"
    directory = "profile"
    site = protocol + "localhost:8000/" + directory

    headers = {
        "Authorization": token
    }

    return requests.get(site, headers=headers)

