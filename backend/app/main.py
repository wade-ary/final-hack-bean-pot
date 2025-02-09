from app.database.database_service import create_user
from app.database.models import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import carbon, location, user_auth # Import API routers
from app.config import settings

app = FastAPI(
    title="Carbon Tracker API",
    description="API for tracking carbon footprint and providing insights",
    version="1.0.0"
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(carbon.router, prefix="/carbon", tags=["Carbon Footprint"])
app.include_router(location.router, prefix="/location", tags=["Location Services"])
app.include_router(user_auth.router, prefix="/user_auth", tags=["User Management"]) 
# Health check endpoint
@app.get("/", tags=["Health"])
async def root():
    return {"message": "Carbon Tracker API is running!"}

@app.post("/signup")
async def signup(user: User):
    user_data = await create_user(user)
    return user_data
