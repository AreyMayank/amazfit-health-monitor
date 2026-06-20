"""
BLE Service Debugger

Lists BLE services, characteristics and descriptors.
"""


import asyncio

from bleak import BleakClient

from src.config import WATCH_ADDRESS


async def main():

    print("Starting service debug...")


    async with BleakClient(
        WATCH_ADDRESS
    ) as client:


        print(
            "Connected:",
            client.is_connected
        )


        for service in client.services:


            print(
                "\nSERVICE:",
                service.uuid
            )


            for char in service.characteristics:


                print(
                    " CHARACTERISTIC:",
                    char.uuid,
                    char.properties
                )


                for descriptor in char.descriptors:


                    print(
                        "    DESCRIPTOR:",
                        descriptor.uuid
                    )


if __name__ == "__main__":


    asyncio.run(
        main()
    )