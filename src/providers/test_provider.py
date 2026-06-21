import asyncio

from src.providers.mock_provider import MockHealthProvider



async def main():


    provider = MockHealthProvider()


    data = await provider.get_health_data()


    print(
        data
    )



asyncio.run(
    main()
)