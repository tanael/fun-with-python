#!/usr/bin/env python3

import asyncio
import time

async def print_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.create_task(print_after(1, 'hello'))
    task2 = asyncio.create_task(print_after(2, 'world'))

    print(f"Starting time: {time.strftime('%X')}") 

    await task2
    await task1

    print(f"Finishing time: {time.strftime('%X')}") 

if __name__ == "__main__":
    asyncio.run(main())
