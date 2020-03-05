#!/usr/bin/env python3

def producer(next_coroutine=None):
    pass

def coro1(next_coroutine=None):
    pass

def coro2(next_coroutine=None):
    pass

def sink():
    pass

def main():
    mysink = sink()
    mysink.send(None)
    c2 = coro2(next_coroutine = mysink)
    c2.__next__()
    c1 = coro1(next_coroutine = coro2)
    c1.__next__()

    producer(next_coroutine = coro1)

if __name__ == "__main__":
    main()
