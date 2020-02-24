#!/usr/bin/env python3

def print_tag(tag):
    print("Searching tag: {}".format(tag))
    idx = 0
    try:
        while True:
            line = (yield "{} I yield".format(idx))
            if tag in line:
                print(line)
            idx += 1
    except GeneratorExit:
        print("Closing the coroutine.")

def main():
    coro = print_tag("hyper")
    caught = coro.__next__() # to start execution of coroutine, till the first yield
    print(caught)
    caught = coro.send("space")
    print(caught)
    caught = coro.send("hyperspace")
    print(caught)
    caught = coro.send("superspace")
    print(caught)
    caught = coro.send("I like hyperspace")
    print(caught)
    coro.close()
    try:
        caught = coro.send("I like hyperspace")
        print(caught)
    except StopIteration:
        print("Coroutine was closed")

if __name__ == "__main__":
    main()
