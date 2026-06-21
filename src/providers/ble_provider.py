"""
BLE Health Provider

Gets available real data directly from Amazfit.
"""


from datetime import datetime


from src.providers.health_provider import HealthProvider

from src.ble.connection import WatchConnection

from src.ble.battery import get_battery



class BLEHealthProvider(HealthProvider):


    async def get_health_data(self):


        watch = WatchConnection()


        try:


            await watch.connect()


            battery = await get_battery(
                watch.client
            )


            return {


                "timestamp": datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),


                "battery": battery,


                # coming from external provider later

                "heart_rate": None,

                "steps": None,

                "spo2": None

            }



        finally:


            await watch.disconnect()