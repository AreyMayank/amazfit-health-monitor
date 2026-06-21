"""
Heart Rate Reader

Amazfit Bip U Pro HR reader
"""


import asyncio


HR_MEASURE_UUID = (
    "00002a37-0000-1000-8000-00805f9b34fb"
)


HR_CONTROL_UUID = (
    "00002a39-0000-1000-8000-00805f9b34fb"
)



async def get_heart_rate(client):


    heart_rate = None


    def callback(sender, data):

        nonlocal heart_rate


        print(
            "HR RAW:",
            list(data)
        )


        if len(data) >= 2:

            heart_rate = data[1]


    try:


        # stop old measurement

        await client.write_gatt_char(
            HR_CONTROL_UUID,
            bytearray([0x15, 0x01])
        )


        await asyncio.sleep(
            1
        )


        # start continuous measurement

        await client.write_gatt_char(
            HR_CONTROL_UUID,
            bytearray([0x15,0x02,0x01])
        )


        await asyncio.sleep(
            1
        )


        # listen

        await client.start_notify(
            HR_MEASURE_UUID,
            callback
        )


        await asyncio.sleep(
            15
        )


        await client.stop_notify(
            HR_MEASURE_UUID
        )


        return heart_rate



    except Exception as e:


        print(
            "HR ERROR:",
            e
        )


        return None