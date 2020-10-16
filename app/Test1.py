import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

def runIt():
    asyncio.run(main())

if __name__ == "__main__":
    runIt()