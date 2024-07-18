import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(10/power)
        print(f"Силач {name} поднял {i} шар", flush=True)
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    strongmans = [('Pasha', 3), ('Denis', 4), ('Apollon', 5)]
    tasks = [asyncio.create_task(start_strongman(*strongman)) for strongman in strongmans]
    [await task for task in tasks]


asyncio.run(start_tournament())
