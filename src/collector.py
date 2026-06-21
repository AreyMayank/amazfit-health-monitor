"""
Continuous Health Collector
"""


import asyncio


from src.providers.ble_provider import BLEHealthProvider

from src.storage.csv_storage import save_health_data



async def main():


    provider = BLEHealthProvider()


    try:


        await provider.connect()


        print(
            "Starting continuous collection..."
        )


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



    except KeyboardInterrupt:


        print(
            "Stopping collector..."
        )



    finally:


        await provider.disconnect()



if __name__ == "__main__":


    asyncio.run(
        main()
    )