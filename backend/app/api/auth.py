from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer
import jwt
from app.config import settings
from bson import ObjectId

security = HTTPBearer()

async def get_current_user(token: str = Security(security)):
    """
    Extracts user data from JWT token.
    """
    try:
        payload = jwt.decode(token.credentials, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # ✅ Convert string user_id to ObjectId
        return {"_id": ObjectId(user_id)}

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")

    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
