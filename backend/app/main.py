from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .auth import signup, login, get_current_user
from .models import User

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Route to sign up new users
@app.post("/signup/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    return signup(db, username, password)

# Route to log in users
@app.post("/login/")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login(db, form_data.username, form_data.password)

# Route to get user profile (protected)
@app.get("/profile/")
def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
        "username": current_user.username,
        "name": current_user.name,
        "last_name": current_user.last_name
    }

# Route to update user profile
@app.put("/profile/")
def update_profile(
    name: str = None,
    last_name: str = None,
    db: Session = Depends(get_db) 
):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if name:
        user.name = name
    if last_name:
        user.last_name = last_name

    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "message": "Profile updated successfully",
        "id": user.id,
        "name": user.name,
        "last_name": user.last_name
    }

