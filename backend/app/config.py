from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# ✅ Load environment variables from .env
load_dotenv()

class Settings(BaseSettings):
    # General Settings
    APP_NAME: str = "Carbon Tracker API"
    VERSION: str = "1.0.0"

    # API Keys
    GOOGLE_MAPS_API_KEY: str = os.getenv("GOOGLE_MAPS_API_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    # Database Config
    MONGO_URI: str = os.getenv("MONGO_URI")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"

# ✅ Initialize settings
settings = Settings()