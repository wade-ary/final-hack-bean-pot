import bcrypt
import jwt
import datetime
from fastapi import APIRouter, HTTPException
from app.database.connections import db
from app.database.models import User
from app.config import settings
from pydantic import BaseModel, EmailStr

router = APIRouter()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM

# ✅ Define request models
class UserSignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


# ✅ SIGNUP Endpoint
@router.post("/signup")
async def signup(user: UserSignupRequest):
    """Registers a new user"""
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password before storing
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    new_user = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,  # ✅ Store as "hashed_password"
        "carbon_logs": []  # Empty list for logs
    }

    result = await db.users.insert_one(new_user)
    return {"message": "User created successfully", "user_id": str(result.inserted_id)}


# ✅ LOGIN Endpoint
@router.post("/login")
async def login(user: UserLoginRequest):
    """Authenticates user and returns JWT token"""
    existing_user = await db.users.find_one({"email": user.email})

    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    print("🛠 DEBUG: Existing User Data →", existing_user)  # ✅ Debugging step

    # Verify password with hashed_password
    if not bcrypt.checkpw(user.password.encode("utf-8"), existing_user["hashed_password"].encode("utf-8")):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Generate JWT Token
    token_data = {
        "user_id": str(existing_user["_id"]),
        "email": existing_user["email"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Token expires in 24 hrs
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {"message": "Login successful", "token": token}
