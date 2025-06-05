import random
import time
import asyncio

async def rainfall_simulation():
    while True:
        random_rainfall = random.randint(0, 100)
        print(f"Simulated rainfall: {random_rainfall} mm")
        await asyncio.sleep(1)