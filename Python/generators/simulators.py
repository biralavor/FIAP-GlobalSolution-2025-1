import random
import asyncio

def rainfall_init(parsed_data: dict) -> dict:
    data_with_rainfall = {}
    for district, neighbor in parsed_data.items():
        data_with_rainfall[district] = []
        for neighbor_name in neighbor:
            data_with_rainfall[district].extend([neighbor_name, 0])
    return data_with_rainfall

async def extreme_rainfall_risk_simulator(parsed_data: dict) -> dict:
    data_with_rainfall = {}
    data_with_rainfall = rainfall_init(parsed_data)
    while True:
        for district, neighbors in data_with_rainfall.items():
            for idx in range(0, len(neighbors), 2):
                rainfall_risk = random.randint(0, 4)
                neighbors[idx + 1] = rainfall_risk
        await asyncio.sleep(1)
        return data_with_rainfall

def incident_simulator(neighborhood_list: dict, data_with_rainfall: dict) -> dict:
    for location in neighborhood_list:
        rainfall_risk = rainfall_risk_getter(location, data_with_rainfall)
        incident = random.randint(0, pow(3, rainfall_risk))
        confidence_level = ""
        if incident >= 15:
            confidence_level = "High"
        elif incident >= 10:
            confidence_level = "Med"
        elif incident >= 5:
            confidence_level = "Low"
        else:
            confidence_level = "-"
        neighborhood_list[location] = [incident, confidence_level]
    return neighborhood_list

def rainfall_risk_getter(location: str, data_with_rainfall: dict) -> int:
    rainfall_risk = 0
    for districts, neighbors in data_with_rainfall.items():
        for idx in range(0, len(neighbors), 2):
            if neighbors[idx] == location:
                rainfall_risk = neighbors[idx + 1]
    return rainfall_risk