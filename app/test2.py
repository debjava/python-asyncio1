import asyncio


async def getData(numValue):
    await asyncio.sleep(numValue)
    return str(numValue)


async def getData1(numValue):
    await asyncio.sleep(2)
    return str(numValue)


async def performAll():
    strValue = await asyncio.gather(getData1(5))
    # It prints: String value:  ['5'] Type of  <class 'list'>
    print("String value: ", strValue, "Type of ", type(strValue))

    listOfValues = await asyncio.gather(getData(5), getData(7), getData(9))
    for i in listOfValues:
        print("Results after waiting: ", i)


def runIt():
    asyncio.run(performAll())


if __name__ == "__main__":
    runIt()
