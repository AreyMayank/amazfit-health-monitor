"""
BLE Connection Manager
"""

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
            "Connection Failed ❌")

        return False


    async def disconnect(self):

        if self.client.is_connected:

            await self.client.disconnect()

            print(
                "Watch Disconnected"
            )