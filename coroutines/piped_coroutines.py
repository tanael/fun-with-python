#!/usr/bin/env python3

def producer(phrase, next_coroutine=None):
    print("Producing tokens")
    tokens = phrase.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()
    print("Token production terminated")

def filter_pattern(pattern="er", next_coroutine=None):
    print("Filtering using pattern")
    try:
        while True:
            token = yield
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with 1st coroutine")
        next_coroutine.close()

def decorate_token(next_coroutine=None):
    print("Decorating token")
    try:
        while True:
            token = yield
            token = ">> {} <<".format(token)
            next_coroutine.send(token)
    except GeneratorExit:
        print("Done with 2nd coroutine")
        next_coroutine.close()

def sink():
    print("Welcome to the sink")
    try:
        while True:
            token = yield
            print(token)
    except GeneratorExit:
        print("Sink terminated")

def main():
    mysink = sink()
    mysink.send(None)
    decotok = decorate_token(next_coroutine = mysink)
    decotok.__next__()
    filpat = filter_pattern(next_coroutine = decotok)
    filpat.__next__()

    phrase = "The Destroyer of Worlds has come, fellow citizens. Show him no mercy!"
    producer(phrase, next_coroutine = filpat)
    print("Demonstration over")

if __name__ == "__main__":
    main()
