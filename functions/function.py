#!/usr/bin/env python3

def mutable_defaults(arg, default_arg=[]):
    default_arg.append("Hello, World!")
    return "arg={}, default_arg={}".format(arg, default_arg)

def print_args(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

def print_arguments(arg, *args, **kwargs):
    print(arg)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print("{} {}".format(key, value))

def main():
    print(mutable_defaults("first"))
    print(mutable_defaults("second"))

    print()

    my_args = ['foo', 'bar', 'zoo']
    print_args(*my_args)

    print()

    my_args = ['a', 2, True]
    my_kwargs = {"one": 1, "two": 2, "three": 3}
    print_arguments(">> arg", *my_args, **my_kwargs)


if __name__ == "__main__":
    main()