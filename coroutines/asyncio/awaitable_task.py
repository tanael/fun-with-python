#!/usr/bin/env python3

import asyncio

async def foobar():
    return 42

async def main():
    task = asyncio.create_task(foobar())
    print(await task)

if __name__ == "__main__":
    asyncio.run(main())
