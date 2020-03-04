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

def repeat(galaxyName, name='johnson', dogName='pegasus'):
    print("That dog's name is {}".format(dogName))
    print("That galaxy's name is {}".format(galaxyName))
    print("That name is {}".format(name))

def wrapping():
    wrapping_var = "wrapping var"

    def wrapped():
        return wrapping_var
    return wrapped

def counter():
    count = 0
    msg = "HALLO"

    def tick():
        nonlocal count
        nonlocal msg
        count += 1
        return count
    return tick

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

    print()

    my_dict = {"galaxyName": "andromeda", "dogName": "cerberus",
            "name": "vega"}
    repeat(**my_dict)

    print()
    foo = wrapping()
    print(foo)
    print(foo())
    cl = foo.__closure__
    print(cl)
    print(cl[0].cell_contents)
    bar = counter()
    print(bar)
    print(bar())
    print(bar())
    print(bar())
    print(bar())
    cl = bar.__closure__
    print(cl)
    print(cl[0].cell_contents)
    print(cl[1].cell_contents)


if __name__ == "__main__":
    main()
