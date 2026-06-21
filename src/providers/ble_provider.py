"""
BLE Health Provider

Maintains continuous Amazfit connection.
"""


from datetime import datetime


from src.providers.health_provider import HealthProvider

from src.ble.connection import WatchConnection

from src.ble.battery import get_battery



class BLEHealthProvider(HealthProvider):


    def __init__(self):

        self.watch = WatchConnection()



    async def connect(self):

        await self.watch.connect()



    async def disconnect(self):

        await self.watch.disconnect()



    async def get_health_data(self):


        battery = await get_battery(
            self.watch.client
        )


        return {

            "timestamp": datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "battery": battery,

            "heart_rate": None,

            "steps": None,

            "spo2": None

        }