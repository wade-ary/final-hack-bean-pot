import googlemaps
from app.config import settings

# Initialize Google Maps client
gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

def calculate_distance(start: str, end: str, mode: str = "driving"):
    """Calculates the distance between two locations."""
    try:
        directions = gmaps.directions(start, end, mode=mode)
        
        if not directions:
            return None
        
        distance_meters = directions[0]['legs'][0]['distance']['value']
        duration_seconds = directions[0]['legs'][0]['duration']['value']

        return {
            "distance_km": round(distance_meters / 1000, 2),
            "duration_minutes": round(duration_seconds / 60, 2),
        }
    
    except Exception as e:
        return {"error": str(e)}
