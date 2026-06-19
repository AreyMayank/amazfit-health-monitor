"""
BLE Connection Manager

Handles smartwatch connection.
"""


import asyncio
from bleak import BleakClient

from src.config import WATCH_ADDRESS



async def connect_watch():

    print(
        "\nConnecting to Amazfit...\n"
    )


    async with BleakClient(
        WATCH_ADDRESS
    ) as client:


        if client.is_connected:

            print(
                "Watch Connected Successfully ✅"
            )


        else:

            print(
                "Connection Failed ❌"
            )



async def main():

    await connect_watch()



if __name__ == "__main__":

    asyncio.run(
        main()
    )