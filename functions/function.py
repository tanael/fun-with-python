#!/usr/bin/env python3

def mutable_defaults(arg, default_arg=[]):
    default_arg.append("Hello, World!")
    return "arg={}, default_arg={}".format(arg, default_arg)

def main():
    print(mutable_defaults("first"))
    print(mutable_defaults("second"))


if __name__ == "__main__":
    main()
