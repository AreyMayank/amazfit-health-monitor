"""
Huami HR Command Test
"""


import asyncio

from bleak import BleakClient

from src.config import WATCH_ADDRESS


COMMAND = (
    "00000008-0000-3512-2118-0009af100700"
)


LISTEN = [

    "00000006-0000-3512-2118-0009af100700",

    "00000007-0000-3512-2118-0009af100700",

    "00000010-0000-3512-2118-0009af100700"

]


def callback(sender, data):

    raw = list(data)


    print(
        "\nFROM:",
        sender
    )

    print(
        "RAW:",
        raw
    )


async def main():

    client = BleakClient(
        WATCH_ADDRESS
    )


    try:

        await client.connect()

        print(
            "Connected"
        )


        for uuid in LISTEN:

            await client.start_notify(
                uuid,
                callback
            )

            print(
                "Listening:",
                uuid
            )


        print(
            "Sending HR start..."
        )


        await client.write_gatt_char(
            COMMAND,
            bytes([0x15,0x02,0x01])
        )


        print(
            "Waiting..."
        )


        await asyncio.sleep(
            60
        )


    finally:

        await client.disconnect()

        print(
            "Disconnected"
        )


asyncio.run(main())