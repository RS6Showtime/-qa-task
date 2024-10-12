from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import get_db
from models import User

# Pre Added
import hashlib
import random
import string

# Max Characters on Postgress DB is 45
MAX_CHARACTERS_AUTH_TOKEN = 35

MIN_CHARACTERS_USERNAME = 3
MAX_CHARACTERS_USERNAME = 24

MIN_CHARACTERS_PASSWORD = 6

MAX_CHARACTERS_NAME = 45
MAX_CHARACTERS_LAST_NAME = 45

def generate_random_auth_token():
    characters = string.ascii_lowercase + string.digits
    length = MAX_CHARACTERS_AUTH_TOKEN
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

def verify_password(plain_password : str, hashed_password : str):
    return hashlib.md5(plain_password.encode('utf-8')).hexdigest() == hashed_password

def get_password_hash(password : str):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# User signup
def signup(db: Session, username: str, password: str):

    length_username = len(username)
    length_password = len(password)

    if length_username < MIN_CHARACTERS_USERNAME or length_username > MAX_CHARACTERS_USERNAME:
        return {"error" : "1", "message" : f"Your username should be between {MIN_CHARACTERS_USERNAME}-{MAX_CHARACTERS_USERNAME} characters."}
    elif length_password < MIN_CHARACTERS_PASSWORD:
        return {"error" : "1", "message" : f"Password is to short. It require at least {MIN_CHARACTERS_PASSWORD} characters."}

    username = username.strip()

    # Check if username is already alocated to someone else
    user_exist = db.query(User).filter(User.username == username).first()

    if user_exist:
        return {"error" : "1", "message" : "Current username already exists. Use something else."}

    # Hash password using MD5
    hashed_password = get_password_hash(password)
    gen_auth_token = ""

    while True:
        gen_auth_token = generate_random_auth_token()

        user = db.query(User).filter(User.auth_token == gen_auth_token).first()
        if user is None:
            break

    # pre-set the data we want to insert
    new_user = User(username=username, hashed_password=hashed_password, auth_token=gen_auth_token)
    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)
        
        # If commit and refresh were successful, the user is valid and successfully inserted
        return {"error" : "0", "message" : "Account created successfully."}
    
    except:
        # If something goes wrong, rollback and return an error message
        db.rollback()
        return {"error" : "1", "message" : "Something went wrong. Please try again later."}


# User login
def login(db: Session, username: str, password: str):

    length_username = len(username)
    length_password = len(password)

    if length_username < 3 or length_username > 24 or length_password < 1:
        return {"error" : "1", "message" : "Invalid length. Username or password to short."}

    username = username.strip()

    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return {"error" : "1", "message" : "Invalid username or password."}
    
    return {"error" : "0", "message" : "You have successfully logged in.", "token" : user.auth_token}

def get_user_via_token(auth_token: str, db: Session):

    # Prevent overflow
    if not auth_token or len(auth_token) > MAX_CHARACTERS_AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="You are not authorized for this action.")

    user = db.query(User).filter(User.auth_token == auth_token).first()

    # In case we hit no user in db
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token or user not found.")

    return user

async def get_current_user(auth_token: str = Header(..., alias="Authorization"), db: Session = Depends(get_db)):
    return get_user_via_token(auth_token, db)


def update_user_profile(db: Session, auth_token: str, name: str, last_name: str):

    max_ch_name = MAX_CHARACTERS_NAME
    max_ch_last = MAX_CHARACTERS_LAST_NAME

    length_name = len(name)
    length_last_name = len(last_name)

    # in case user will send others longs data instead of the needed.
    if length_name < 1 or length_name > max_ch_name:
        return {"error" : "1", "message": f"Invalid First Name. We except 1-{max_ch_name} characters"}
    elif length_last_name < 1 or length_last_name > max_ch_last:
        return {"error" : "1", "message": f"Invalid last name We except 1-{max_ch_last} characters"}

    user = get_user_via_token(auth_token, db)

    if user is None:
        return {"error" : "1", "message": "User not found"}

    if name:
        user.name = name
    if last_name:
        user.last_name = last_name

    try:
        db.commit()
        db.refresh(user)

        return {"error" : "0", "message" : "Profile updated successfully."}
    except:
        return {"error" : "1", "message" : "Something went wrong while trying to update your profile. Please try again later"}
    
