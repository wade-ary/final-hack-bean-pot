import motor.motor_asyncio
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get MongoDB URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# ✅ Connect to MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["carbon_footprint"]

# ✅ Collections (Tables)
users_collection = db["users"]
carbon_collection = db["carbon_footprints"]

