#!/usr/bin/env python3

import datetime
from functools import wraps

def logger(func_to_decorate):

    @wraps(func_to_decorate)
    def func_wrapper(*args, **kwargs):

        print("Calling function: {} at {}".format(func_to_decorate.__name__,
              datetime.datetime.now()))

        func_to_decorate(*args, **kwargs)

        print("Finished calling: {} at {}".format(func_to_decorate.__name__,
              datetime.datetime.now()))

    return func_wrapper

def print_hello():
    print("Hello you!!")

@logger
def print_goodbye():
    print("Bye bye!!")

def main():
    decorated_func = logger(print_hello)
    print("The decorated function: {}".format(decorated_func))
    decorated_func()
    print_goodbye()

if __name__ == "__main__":
    main()
