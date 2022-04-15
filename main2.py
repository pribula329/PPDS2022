from time import sleep,time
import asyncio

async def cooking(cook):
    for i in range(1,4):
        print(f"Kuchar {cook} vari")
        await asyncio.sleep(i/3)
        print(f"Kuchar {cook} dovaril {i} jedlo")



async def main():
    pass

asyncio.run(main())