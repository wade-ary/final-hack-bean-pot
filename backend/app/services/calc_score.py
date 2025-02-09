from app.database.database_service import update_form_score
from app.services.calc_emissions import calculate_total_log_emissions
from typing import Any, Dict

def calculate_form_score(carbon_log: Dict[str, Any]) -> int:
    """
    Calculates a score out of 100 for the travel log based on emissions and sustainability choices
    and updates the total_score field in the database.
    """
    total_co2 = calculate_total_log_emissions(carbon_log)  # Get emissions in kg
    
    # Base penalty (higher emissions = lower score)
    base_penalty = total_co2 * 2.5  # Adjust weight if needed

    # Bonus points for sustainable actions
    sustainability_bonus = 0

    # Walking/Biking Bonus
    if carbon_log.get("active_travel", {}).get("walked_or_biked", False):
        sustainability_bonus += 10

    # Public Transport Bonus
    if carbon_log.get("public_transport", {}).get("used_public_transport", False):
        sustainability_bonus += 5

    # Carpooling Bonus
    car_usage = carbon_log.get("car_usage", {})
    if car_usage:
        passengers = car_usage.get("carpool_status", 0)
        if passengers >= 1:
            sustainability_bonus += min(passengers * 3, 10)  # Max +10 pts

    # Electric Vehicle Bonus
    if car_usage.get("make", "").lower() == "tesla" or car_usage.get("fuel_type", "").lower() == "ev":
        sustainability_bonus += 8

    # User-reported Sustainable Actions
    if carbon_log.get("sustainable_action_tried"):
        sustainability_bonus += 5

    # Calculate final score (ensure it's between 0 and 100)
    score = max(100 - base_penalty + sustainability_bonus, 0)
    score = int(min(score, 100))  # Ensure max score is 100

    # Update the total_score field in the database
    update_form_score(carbon_log["log_id"], score)
    
    return score
