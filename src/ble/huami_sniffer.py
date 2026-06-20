"""
Huami Protocol Sniffer

Captures Amazfit private health packets.
"""


import asyncio

from bleak import BleakClient

from src.config import WATCH_ADDRESS

from datetime import datetime


HUAMI_CHANNELS = [

    "00000006-0000-3512-2118-0009af100700",

    "00000007-0000-3512-2118-0009af100700",

    "00000010-0000-3512-2118-0009af100700"

]



def packet_handler(sender, data):


    raw = list(data)


    print(
        "\n===================="
    )


    print(
        "TIME:",
        datetime.now()
        .strftime("%H:%M:%S")
    )


    print(
        "CHANNEL:",
        sender
    )


    print(
        "RAW:",
        raw
    )


    for index, value in enumerate(raw):


        if 40 <= value <= 200:


            print(
                "Candidate:",
                "index:",
                index,
                "value:",
                value
            )




async def main():


    client = BleakClient(
        WATCH_ADDRESS
    )


    try:


        print(
            "Connecting..."
        )


        await client.connect()


        print(
            "Connected:",
            client.is_connected
        )



        for channel in HUAMI_CHANNELS:


            try:


                await client.start_notify(
                    channel,
                    packet_handler
                )


                print(
                    "Listening:",
                    channel
                )


            except Exception as error:


                print(
                    "Channel failed:",
                    channel,
                    error
                )



        print(
            "\nStart Heart Rate on watch ❤️"
        )


        await asyncio.sleep(
            120
        )



    finally:


        await client.disconnect()


        print(
            "Disconnected"
        )




if __name__ == "__main__":


    asyncio.run(
        main()
    )