#!/usr/bin/env python3

import asyncio

async def simple():
    print("foo")
    await asyncio.sleep(1)
    print("bar")

def main():
    asyncio.run(simple())

if __name__ == "__main__":
    main()
