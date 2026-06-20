import asyncio

from bleak import BleakClient

from src.config import WATCH_ADDRESS


HR_UUID = (
    "00002a37-0000-1000-8000-00805f9b34fb"
)

CTRL_UUID = (
    "00002a39-0000-1000-8000-00805f9b34fb"
)


async def main():

    async with BleakClient(WATCH_ADDRESS) as client:

        print(
            "Connected:",
            client.is_connected
        )


        # start HR measurement

        print(
            "Starting HR sensor..."
        )

        try:

            await client.write_gatt_char(
                CTRL_UUID,
                bytes([0x01])
            )

            print(
                "Start command sent"
            )


        except Exception as e:

            print(
                "Start failed:",
                e
            )


        await asyncio.sleep(3)



        def callback(sender, data):

            print(
                "❤️ HR RAW:",
                list(data)
            )


            if len(data) >= 2:

                print(
                    "HEART RATE:",
                    data[1],
                    "BPM"
                )



        print(
            "Listening..."
        )


        await client.start_notify(
            HR_UUID,
            callback,
            force_indicate=True
        )


        await asyncio.sleep(
            30
        )


        await client.stop_notify(
            HR_UUID
        )


asyncio.run(main())