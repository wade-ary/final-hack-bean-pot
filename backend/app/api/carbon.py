import uuid
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.database.connections import db
from app.database.models import CarbonFootprint
from typing import Dict, Any
import datetime
from bson import ObjectId
from app.services.calc_score import calculate_form_score
from app.services.calc_emissions import calculate_total_log_emissions
import jwt
from app.config import settings
from app.services.openai_services import analyze_carbon_footprint
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Extracts the user ID from the JWT token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        return payload.get("user_id")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/submit")
async def submit_carbon_footprint(data: Dict[str, Any], user_id: str = Depends(get_current_user)):
    """
    Handles user carbon footprint submission.
    1. Stores the form data as a new CarbonFootprint log.
    2. Calculates the user's carbon score.
    3. Links the log to the user's history.
    """
    try:
        # ✅ Assigning form values
        log_id = str(uuid.uuid4())  # ✅ Generate a random log_id

        new_log = CarbonFootprint(
            log_id=log_id,
            user_id=ObjectId(user_id),
            date=datetime.datetime.utcnow().strftime("%Y-%m-%d"),
            travel=data.get("travel", []),
            car_usage=data.get("car_usage", {}),
            public_transport=data.get("public_transport", {}),
            active_travel=data.get("active_travel", {}),
            consider_other_transport=data.get("consider_other_transport"),
            small_transport_change=data.get("small_transport_change"),
            sustainable_action_tried=data.get("sustainable_action_tried"),
            eco_friendly_choice_proud=data.get("eco_friendly_choice_proud"),
            total_carbon_score=calculate_total_log_emissions(data), 
            total_score=calculate_form_score(data),
            ai_feedback= analyze_carbon_footprint(data)
        )

        # ✅ Save to MongoDB
        result = await db.carbon_logs.insert_one(new_log.dict())

        # ✅ Update User Record: Append log_id to `carbon_emissions`
        await db.users.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"carbon_emissions": log_id}}
        )

        return {
            "message": "Carbon footprint submitted successfully",
            "log_id": log_id,
            "carbon_score": new_log.total_carbon_score,
            "ai_feedback": new_log.ai_feedback
        }

    except Exception as e:
        print("❌ Error:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")




