from fastapi import APIRouter, HTTPException
from app.services.location import calculate_distance

router = APIRouter()

@router.get("/calculate_distance")
def get_distance(start: str, end: str, mode: str = "driving"):
    """
    API endpoint to calculate the distance between two locations.
    Example usage: /calculate_distance?start=Boston,MA&end=New York,NY&mode=driving
    """
    result = calculate_distance(start, end, mode)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result

