import asyncio


async def task(taskNo, timeToWait):
    print("Task - "+str(taskNo)+" initiated")
    await asyncio.sleep(timeToWait)
    print("Task - "+str(taskNo)+" completed")
    return str(taskNo)

async def performTask():
    task1 = asyncio.create_task(task(1, 3))
    task2 = asyncio.create_task(task(2, 5))
    task3 = asyncio.create_task(task(3, 7))

    a, b, c = await asyncio.gather(task1, task2, task3)

    print("---------- All validations completed -------")
    print("A: ", a)
    print("B: ", b)
    print("C: ", c)

def performAll():
    asyncio.run(performTask())

if __name__ == "__main__":
    performAll()