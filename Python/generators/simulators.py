import random
import asyncio

def rainfall_init(parsed_data):
    data_with_rainfall = {}
    for district, neighbor in parsed_data.items():
        data_with_rainfall[district] = []
        for neighbor_name in neighbor:
            data_with_rainfall[district].extend([neighbor_name, 0])
    return data_with_rainfall

async def extreme_rainfall_risk_simulator(data_with_rainfall):
    while True:
        # print(f"Simulated rainfall risk: {rainfall_risk} mm")
        for district, neighbors in data_with_rainfall.items():
            for idx in range(0, len(neighbors), 2):
                rainfall_risk = random.randint(0, 4)
                neighbors[idx + 1] = rainfall_risk
        await asyncio.sleep(1)
        return data_with_rainfall