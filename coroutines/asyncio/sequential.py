#!/usr/bin/env python3

import asyncio
import time

async def print_after(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    print(f"Starting time: {time.strftime('%X')}") 

    await print_after(2, 'hello')
    await print_after(1, 'world')

    print(f"Finishing time: {time.strftime('%X')}") 

if __name__ == "__main__":
    asyncio.run(main())
