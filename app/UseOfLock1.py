import asyncio

async def doSomeCritical():
    lock = asyncio.Lock()
    async with lock:
        try:
            print("Going to perform critical operation")
            await asyncio.sleep(3)  # Critical operation
            print("Operation completed")
            return "some value"
        finally:
            lock.release()



async def performCriticalOperation():
    lock = asyncio.Lock()
    await lock.acquire()
    print('lock acquired: {}'.format(lock.locked()))
    finished = await asyncio.wait([doSomeCritical()])
    print("Returned Value: ", finished.pop().result())
    # lock.release()


def perform():
    asyncio.run(doSomeCritical())


if __name__ == "__main__":
    perform()
