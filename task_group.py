import asyncio


async def fetch_data(delay, id):
    print('Fetching data for id:', id)
    await asyncio.sleep(delay)
    print('Data fetched')
    return {'data': 'some data', 'id': id}


async def main():
    tasks = []

    # comes with builtin error handling
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    print(results)


asyncio.run(main())
