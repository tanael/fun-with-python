#!/usr/bin/env python3

def print_tag(tag):
    print("Searching tag: {}".format(tag))
    idx = 0
    try:
        while True:
            print("Reaching the yield statement")
            line = (yield "{} I yield".format(idx))
            print("Passed the yield statement")
            if tag in line:
                print("Matched the tag: {}".format(line))
            idx += 1
    except GeneratorExit:
        print("Closing the coroutine.")

def main():
    coro = print_tag("hyper")

    # You can either use __next__() or send a None value
    # caught = coro.__next__() # to start execution of coroutine, till the first yield
    caught = coro.send(None)
    print(">> 0 Caught this: {}".format(caught))

    caught = coro.send("space")
    print(">> 1 Caught this: {}".format(caught))
    caught = coro.send("hyperspace")
    print(">> 2 Caught this: {}".format(caught))
    caught = coro.send("superspace")
    print(">> 3 Caught this: {}".format(caught))
    caught = coro.send("I like hyperspace")
    print(">> 4 Caught this: {}".format(caught))
    coro.close()
    try:
        caught = coro.send("I like hyperspace a lot")
        print(">> 5 Caught this: {}".format(caught))
    except StopIteration:
        print("Coroutine was closed")

if __name__ == "__main__":
    main()
