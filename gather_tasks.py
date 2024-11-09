import asyncio


async def fetch_data(delay, id):
    print('Fetching data for id:', id)
    await asyncio.sleep(delay)
    print('Data fetched')
    return {'data': 'some data', 'id': id}


async def main():
    print('start of the main coroutine')
    results = await asyncio.gather(asyncio.create_task(fetch_data(2, 1)), asyncio.create_task(fetch_data(1, 2)))

    for result in results:
        print(result)

asyncio.run(main())
