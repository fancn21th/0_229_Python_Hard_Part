import asyncio


async def foo(txt):
    print(txt)
    await asyncio.sleep(10)


async def main():
    print("start ...")
    task = asyncio.create_task(foo("Hello"))
    # await task
    await asyncio.sleep(0.5)
    print("... end")


# Python 3.7+

asyncio.run(main())
