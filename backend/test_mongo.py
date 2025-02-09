import motor.motor_asyncio
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# ✅ Connect to MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["carbon_footprint"]

async def test_connection():
    try:
        await db.command("ping")
        print("✅ Connected to MongoDB Atlas!")
    except Exception as e:
        print("❌ MongoDB Connection Failed:", str(e))  # 🔍 Print full error

import asyncio
asyncio.run(test_connection())

