"""
Battery Reader

Reads battery percentage from connected watch.
"""


BATTERY_UUID = (
    "00002a19-0000-1000-8000-00805f9b34fb"
)


async def get_battery(client):
    """
    Read battery percentage.

    Args:
        client: active BleakClient connection

    Returns:
        int: battery percentage
    """


    battery_data = await client.read_gatt_char(
        BATTERY_UUID
    )


    battery_percentage = int(
        battery_data[0]
    )


    return battery_percentage