import asyncio


async def waiter(event):
    print("Waiting for event to be set")
    await event.wait()
    print("Event is set, continuing execution")


async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("Event has been set")


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())
