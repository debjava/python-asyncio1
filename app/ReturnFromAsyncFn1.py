import asyncio


async def runValdn1():
    await asyncio.sleep(2)  # wait for 2 seconds
    print("Validation - 1 completed")
    return "Completed-1"


async def runValdn2():
    await asyncio.sleep(3)  # wait for 3 seconds
    print("Validation - 2 completed")
    return "Completed-2"


async def runValidn3():
    await asyncio.sleep(5)  # wait for 5 seconds
    print("Validation - 3 - completed")
    return "Completed-3"


async def runAllValdns():
    # await runValdn1()
    # await runValdn2()
    # await runValidn3()
    a, b, c = await runValdn1(), await runValdn2(), await runValidn3()
    print("---------- All validations completed -------")
    print("A: ", a)
    print("B: ", b)
    print("C: ", c)


def performAll():
    asyncio.run(runAllValdns())

if __name__ == "__main__":
    performAll()
