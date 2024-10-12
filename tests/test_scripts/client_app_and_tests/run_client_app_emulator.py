import os
from scripts.login import login_user
from scripts.signup import signup_user
from scripts.view_profile import view_user_profile
from scripts.update_profile import update_user_profile

logged_in = False
prefixes = ("Welcome", "Hey")

__ERROR_NO__ = 0
__ERROR_YES__ = 1
__ERROR_INV_SES__ = 2

__EXIT__ = 0
__SIGNUP__ = 1
__LOGIN__ = 2
__PROFILE__ = 1
__UP_PROFILE__ = 2

os_type = os.name
token = ""

def clear_console():
    global os_type
    if os_type == "nt":
        os.system("cls")
    else:
        os.system("clear")


def handle_response_code(error_id : int):
    global logged_in
    if error_id == __ERROR_NO__:
        logged_in = True
    elif error_id == __ERROR_YES__:
        logged_in = False
    elif error_id == __ERROR_INV_SES__:
        logged_in = False

def login_signup_inputs():
    username = input("Please insert username: ")
    password = input("Please insert password: ")

    return (username, password)

def update_profile_inputs():
    name = input("Insert First Name: ")
    last_name = input("Insert Last Name: ")

    return (name, last_name)

while True:
    if logged_in == False:
        print("Welcome!")
    else:
        print("Hey,")

    print("What do you wish to do?\n")

    if logged_in == False:
        print("[1] SignUp")
        print("[2] Login")
    else:
        print("[1] View Profile")
        print("[2] Update Profile")

    print("\n[0] Exit\n")

    try:
        option = int(input("Enter Option: "))
    except ValueError:
        print("Please enter a valid option.")
        continue
    
    if option == __EXIT__:
        os._exit(1)

    # User is not Logged In
    if logged_in == False:
        if option == __SIGNUP__:
            clear_console()
            username, password = login_signup_inputs()

            result = signup_user(username, password)

            json_data = result.json()

            clear_console()

            # Show the response message
            try:
                print(json_data['message'] + "\n")
            except:
                print("Something went wrong. No valid response from the server\n")
        elif option == __LOGIN__:
            clear_console()
            username, password = login_signup_inputs()

            result = login_user(username, password)

            json_data = result.json()

            clear_console()
            try:
                handle_response_code(int(json_data['error']))
                print(json_data['message'] + "\n")

                if 'token' in json_data:
                    token = json_data['token']

            except:
                print("Something went wrong. No valid response from the server\n")
        else:
            clear_console()
    # User is logged In
    else:
        if option == __PROFILE__:
            clear_console()

            result = view_user_profile(token)

            json_data = result.json()
            
            if result.status_code == 200:
                if 'username' in json_data and 'name' in json_data and 'last_name' in json_data:
                    print(f"Username: {json_data['username']}")
                    print(f"Name: {json_data['name']}")
                    print(f"Last Name: {json_data['last_name']}\n")
                elif 'error' in json_data and 'message' in json_data:
                    handle_response_code(json_data['error'])
                    print(json_data['message'] + "\n")
                else:
                    print("Something went wrong. No valid response from the server\n")
            else:
                if 'details' in json_data:
                    print(json_data['details'])
                else:
                    print("Something went wrong. No valid response from the server\n")

        elif option == __UP_PROFILE__:
            clear_console()

            first_name, last_name = update_profile_inputs()

            clear_console()

            result = update_user_profile(token, first_name, last_name)

            json_data = result.json()
            
            if result.status_code == 200:
                if 'error' in json_data and 'message' in json_data:
                    handle_response_code(json_data['error'])
                    print(json_data['message'] + "\n")
                else:
                    print("Something went wrong. No valid response from the server\n")
            else:
                if 'details' in json_data:
                    print(json_data['details'])
                else:
                    print("Something went wrong. No valid response from the server\n")

