from typing import Dict, Any
import math
import pandas as pd

from app.services.location import calculate_distance  

car_emissions_csv = "backend/app/services/CO2 Emissions_Canada.csv"

def load_car_emissions():
    """Loads car emissions data from CSV into a Pandas DataFrame."""
    try:
        df = pd.read_csv(car_emissions_csv)
        return df
    except Exception as e:
        return {"error": str(e)}

def find_car_emission(make: str, model: str):
    """
    Finds CO2 emissions for a given car make and model.
    Returns emissions in grams per km.
    """
    df = load_car_emissions()
    
    if isinstance(df, dict):  # Error handling if CSV failed to load
        return df

    # Filter by Make and Model (case-insensitive)
    car = df[(df["Make"].str.lower() == make.lower()) & (df["Model"].str.lower() == model.lower())]

    if car.empty:
        return {"error": "Car not found in database."}
    
    return car.iloc[0]["CO2 Emissions(g/km)"]  # Return CO2 emissions per km 

def calculate_car_footprint(start: str, end: str, make: str, model: str) -> float:
    """
    Computes and returns the total carbon footprint (kg CO₂) for a trip.
    """

    # Get CO2 emissions per km for the car
    emissions_per_km = find_car_emission(make, model)
    
    if isinstance(emissions_per_km, dict):  # Handle errors
        return -1  # Return -1 if car not found

    # Get travel distance
    distance_data = calculate_distance(start, end)
    
    if "error" in distance_data:
        return -1  # Return -1 if distance calculation failed

    distance_km = distance_data["distance_km"]
    
    # Compute total emissions (convert g/km to kg)
    total_emissions_kg = round((distance_km * emissions_per_km) / 1000, 2)

    return total_emissions_kg  # Return only the emissions number

def calculate_total_log_emissions(carbon_log: Dict[str, Any]) -> float:
    """
    Computes the total carbon footprint score (kg CO₂) for an entire log entry.
    """

    total_emissions = 0.0
    
    ### 1. **Process Travel Data (Supports Multiple Entries)**
    travel_entries = carbon_log.get("travel", [])
    for travel_data in travel_entries:
        mode_of_transport = travel_data.get("mode_of_transport", "").lower()
        start_location = travel_data.get("start_location", "")
        end_location = travel_data.get("end_location", "")
        make = travel_data.get("make", "")
        model = travel_data.get("model", "")

        # If user traveled using a car, calculate emissions based on car model
        if mode_of_transport == "car" and make and model:
            emissions = calculate_car_footprint(start_location, end_location, make, model)
            if emissions != -1:
                total_emissions += emissions

    ### 2. **Public Transport Usage**
    public_transport = carbon_log.get("public_transport", {})
    if public_transport.get("used_public_transport", False):
        transport_type = public_transport.get("transport_type", "").lower()
        
        # Estimate distance based on last travel entry (if exists)
        if travel_entries:
            last_trip = travel_entries[-1]
            start_location = last_trip.get("start_location", "")
            end_location = last_trip.get("end_location", "")
            distance_data = calculate_distance(start_location, end_location)
            if "error" not in distance_data:
                distance_km = distance_data["distance_km"]
                if transport_type == "bus":
                    total_emissions += round(distance_km * 0.08, 2)  # 80g/km per passenger
                elif transport_type == "train":
                    total_emissions += round(distance_km * 0.04, 2)  # 40g/km per passenger

    ### 3. **Walking/Biking (Zero Emissions)**
    active_travel = carbon_log.get("active_travel", {})
    if active_travel.get("walked_or_biked", False):
        total_emissions += 0  # No emissions


    # Update the log's total_carbon_score directly
    carbon_log["total_carbon_score"] = round(total_emissions, 2)

    return carbon_log["total_carbon_score"]  # Return final total CO2 emissions (kg)

