import asyncio

async def fetch_data(delay, id):
    print('Fetching data for id:', id)
    await asyncio.sleep(delay)
    print('Data fetched')
    return {'data': 'some data', 'id': id}

async def main():
    print('start of the main coroutine')
    task1 = fetch_data(2,1)
    task2 = fetch_data(1,2)
    
    result1 = await task1
    result2 = await task2

    print(f'Received result: {result1}')
    print(f'Received result: {result2}')

asyncio.run(main())
