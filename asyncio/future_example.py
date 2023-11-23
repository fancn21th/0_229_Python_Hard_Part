import asyncio


async def fake_fetch():
    print("start fetching")
    await asyncio.sleep(1)
    print("done fetching")
    return {"data": 1}


async def do_something():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(fake_fetch())
    task2 = asyncio.create_task(do_something())

    value1 = await task1

    print(value1)

    await task2


asyncio.run(main())
