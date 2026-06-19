"""
Health Data Collector

Continuously collects smartwatch data.
"""


import asyncio

from datetime import datetime

from src.ble.connection import WatchConnection
from src.ble.battery import get_battery


COLLECT_INTERVAL = 5


async def collect_data():

    watch = WatchConnection()


    connected = await watch.connect()


    if not connected:

        print(
            "Cannot start collector"
        )

        return


    try:

        while True:


            battery = await get_battery(
                watch.client
            )


            health_data = {

                "timestamp": datetime.now()
                .strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "battery": battery,

                "heart_rate": None,

                "steps": None,

                "spo2": None

            }


            print(
                health_data
            )


            await asyncio.sleep(
                COLLECT_INTERVAL
            )


    except KeyboardInterrupt:


        print(
            "\nCollector stopped"
        )


    finally:


        await watch.disconnect()



if __name__ == "__main__":


    asyncio.run(
        collect_data()
    )