import asyncio


from src.providers.ble_provider import BLEHealthProvider



async def main():


    provider = BLEHealthProvider()


    data = await provider.get_health_data()


    print(
        data
    )



asyncio.run(
    main()
)