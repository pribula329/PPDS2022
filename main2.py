from time import sleep,time
import asyncio

async def cooking(cook):
    for i in range(1,4):
        print(f"Kuchar {cook} vari")
        await asyncio.sleep(i/3)
        print(f"Kuchar {cook} dovaril {i} jedlo")



async def main():
    start_time = time()
    await asyncio.gather(cooking('Lukas'),cooking('Peter'), cooking('Erik'))
    cas = time() - start_time
    print(f"Celkovy cas varenia: {cas:.1f}")

asyncio.run(main())