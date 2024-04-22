## Using asyncio.gather()
import asyncio

async def my_task(num):
    print(f"my_task({num})")
    await asyncio.sleep(num)
    return f"Task {num} is done"

async def main_gather():
    tasks = [my_task(1), my_task(2), my_task(3)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

async def main_wait():
    coros = [my_task(1), my_task(2), my_task(3)] # passing coroutines directly is deprecated and will be removed in py.3.11
    tasks = [asyncio.create_task(coro) for coro in coros]
    done, pending = await asyncio.wait(tasks)
    for task in done:
        result = await task
        print(result)

async def main_as_completed():
    tasks = [my_task(1), my_task(2), my_task(3)]

    for future in asyncio.as_completed(tasks):
        result = await future
        print(result)

asyncio.run(main_gather())
asyncio.run(main_wait())
asyncio.run(main_as_completed())



