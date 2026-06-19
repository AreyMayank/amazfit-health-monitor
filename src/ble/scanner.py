"""
BLE Scanner Module

Responsible for discovering nearby Bluetooth
Low Energy devices.
"""

import asyncio
from bleak import BleakScanner


SCAN_TIMEOUT = 10


async def scan_devices():
    """
    Scan nearby BLE devices.

    Returns:
        list: discovered BLE devices
    """

    print("\n🔍 Scanning BLE devices...\n")

    devices = await BleakScanner.discover(
        timeout=SCAN_TIMEOUT
    )


    if not devices:
        print("No BLE devices found.")
        return []


    return devices



def display_devices(devices):
    """
    Display BLE devices.
    """

    for index, device in enumerate(devices):

        print(
            f"""
Device {index + 1}

Name:
{device.name}

Address:
{device.address}

-------------------------
"""
        )



async def main():

    devices = await scan_devices()

    display_devices(
        devices
    )



if __name__ == "__main__":

    asyncio.run(
        main()
    )