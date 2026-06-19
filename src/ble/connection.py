"""
BLE Connection Manager

Handles connection with Amazfit smartwatch.
"""


import asyncio

from bleak import BleakClient

from src.config import WATCH_ADDRESS



class WatchConnection:


    def __init__(self):

        self.client = BleakClient(
            WATCH_ADDRESS
        )



    async def connect(self):

        print(
            "\nConnecting to watch...\n"
        )


        await self.client.connect()


        if self.client.is_connected:

            print(
                "Watch Connected Successfully ✅"
            )

            return True


        print(
            "Connection Failed ❌"
        )

        return False



    async def disconnect(self):

        if self.client.is_connected:

            await self.client.disconnect()

            print(
                "Watch Disconnected"
            )



async def main():


    watch = WatchConnection()


    connected = await watch.connect()


    if connected:

        print(
            "Ready for data collection"
        )


    await watch.disconnect()



if __name__ == "__main__":

    asyncio.run(
        main()
    )