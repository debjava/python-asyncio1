import asyncio

async def getData(numValue):
    await asyncio.sleep(numValue)
    return "Task-" + str(numValue)

async def perform():
    tasks = [getData(3), getData(5), getData(7)]
    finished, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for p in pending:
        p.cancel()
    try:
        print("Which one completed first: ", finished.pop().result())
    except NotImplementedError as e:
        raise e
    except:
        print("Do nothing")


async def runIt():
    await perform()


if __name__ == '__main__':
    # asyncio.run(perform())
    asyncio.run(runIt())
