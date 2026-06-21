"""
Mock Health Provider

Simulates smartwatch data.
"""


import random

from datetime import datetime


from src.providers.health_provider import HealthProvider



class MockHealthProvider(HealthProvider):


    async def get_health_data(self):


        return {


            "timestamp": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


            "battery": random.randint(
                60,
                100
            ),


            "heart_rate": random.randint(
                65,
                100
            ),


            "steps": random.randint(
                1000,
                10000
            ),


            "spo2": random.randint(
                95,
                100
            )

        }