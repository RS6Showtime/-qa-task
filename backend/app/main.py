from fastapi import FastAPI, Depends, Header
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from pydantic import BaseModel
from auth import signup, login, get_current_user, update_user_profile
from models import User

# This will prevent others from directory discovery and requests enumerating
# And also required data
# Update: old topic, it require BaseSettings to be loaded from pydantic-settings lib

app = FastAPI(docs_url=None, redoc_url=None)

# Create the database tables
Base.metadata.create_all(bind=engine)

class UserAuth(BaseModel):
    username: str
    password: str

# Route to sign up new users
@app.post("/signup/")
def create_user(user: UserAuth, db: Session = Depends(get_db)):
    return signup(db, user.username, user.password)

# Route to log in users
@app.post("/login/")
def login_user(user: UserAuth, db: Session = Depends(get_db)):
    return login(db, user.username, user.password)

# Route to get user profile
@app.get("/profile/")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "error" : "0",
        "username": current_user.username,
        "name": current_user.name,
        "last_name": current_user.last_name
    }

class UserInfo(BaseModel):
    name: str
    last_name: str

# Route to update user profile
@app.post("/profile/")
def update_profile(user_info: UserInfo, auth_token: str = Header(..., alias="Authorization"), db: Session = Depends(get_db)):
    return update_user_profile(db, auth_token, user_info.name, user_info.last_name)