from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Any, Dict, List, Optional
from bson import ObjectId
from pydantic import BaseModel
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from datetime import datetime

class PyObjectId(str):
    """Custom Pydantic field for MongoDB ObjectId."""

    @classmethod
    def validate(cls, value, info):
        """Ensures the value is a valid MongoDB ObjectId."""
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return str(value)

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        """Ensures compatibility with Pydantic v2 schema."""
        return core_schema.str_schema()

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        """Returns JSON schema format."""
        return JsonSchemaValue(type="string")


# User Model
class User(BaseModel):
    user_id: Optional[int] = None
    username: str
    email: EmailStr
    password: str
    carbon_emissions: List[PyObjectId] = []  

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}

class CarbonFootprint(BaseModel):
    log_id: Optional[str] = Field(default=None)
    user_id: ObjectId
    date: Optional[str] = None  # Keeping it Optional to allow auto-generated dates

    # Travel History: Allows multiple trips in one log
    travel: List[Dict[str, str]] = Field(default_factory=list)  
    # Example entry: {"start_location": "A", "end_location": "B", "mode_of_transport": "Car"}

    # Car Usage
    car_usage: Optional[Dict[str, Any]] = Field(default_factory=dict)  
    # Example: {"make": "Toyota", "model": "Camry", "carpool_status": 2, "route_efficiency_score": 4}

    # Public Transport & Shared Rides
    public_transport: Optional[Dict[str, Any]] = Field(default_factory=dict)  
    # Example: {"used_public_transport": True, "transport_type": "Bus"}

    # Walking/Biking
    active_travel: Optional[Dict[str, Any]] = Field(default_factory=dict)  
    # Example: {"walked_or_biked": True}

    # Sustainability Questions
    consider_other_transport: Optional[str] = None
    small_transport_change: Optional[str] = None
    sustainable_action_tried: Optional[str] = None
    eco_friendly_choice_proud: Optional[str] = None

    # Total Carbon Score Calculation
    total_carbon_score: float = 0.0  # Auto-calculated based on user inputs
    total_score: float = 0.0
    ai_feedback: Optional[str] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

   

    

   

    
