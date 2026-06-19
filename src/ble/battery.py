"""
Battery Reader Module

Reads battery percentage from BLE device.
"""


import asyncio

from bleak import BleakClient

from src.config import WATCH_ADDRESS


BATTERY_UUID = (
    "00002a19-0000-1000-8000-00805f9b34fb"
)



async def read_battery():


    async with BleakClient(
        WATCH_ADDRESS
    ) as client:


        print(
            "\nConnected to watch ✅"
        )


        battery_data = await client.read_gatt_char(
            BATTERY_UUID
        )


        battery_percentage = int(
            battery_data[0]
        )


        print(
            f"Battery Level: {battery_percentage}% 🔋"
        )


        return battery_percentage




async def main():

    await read_battery()



if __name__ == "__main__":

    asyncio.run(
        main()
    )