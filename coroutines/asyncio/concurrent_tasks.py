#!/usr/bin/env python3

import asyncio
import time

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    print(f"Starting time: {time.strftime('%X')}") 
    await asyncio.gather(
        factorial("Foo", 2),
        factorial("Bar", 4),
        factorial("Eta", 5),
        factorial("Cho", 7),
        factorial("Ama", 3),
    )
    print(f"Finishing time: {time.strftime('%X')}") 

if __name__ == "__main__":
    asyncio.run(main())
