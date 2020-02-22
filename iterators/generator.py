#!/usr/bin/env python3

def generate_fibonacci(max):
    first, second = 0, 1
    while first < max:
        yield first
        first, second = second, first + second

def main():
    print("\nLimited Fibonacci sequence using a generator:")
    for num in generate_fibonacci(500):
        print(num)

if __name__ == "__main__":
    main()
