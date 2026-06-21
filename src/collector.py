"""
Health Data Collector

Collects health data from providers.
"""


import asyncio


from src.providers.ble_provider import BLEHealthProvider

from src.storage.csv_storage import save_health_data



async def main():


    provider = BLEHealthProvider()


    while True:


        data = await provider.get_health_data()


        print(
            data
        )


        save_health_data(
            data
        )


        await asyncio.sleep(
            10
        )



if __name__ == "__main__":


    asyncio.run(
        main()
    )