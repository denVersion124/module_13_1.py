import asyncio
async def  start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    k = 0
    for i in range(1, 6):
        k+=1

        await asyncio.sleep(5/power)
        print(f"Силач {name} поднял {k} шар.")
    print(f"Силач {name} закончил соревнования.")
async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman("pasha", 3)),
        asyncio.create_task(start_strongman("denis", 4)),
        asyncio.create_task(start_strongman("sergei", 5))
    ]
    await asyncio.gather(*tasks)
asyncio.run((start_tournament()))