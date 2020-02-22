#!/usr/bin/env python3

class Fibonacci:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.first = 0
        self.second = 1
        return self

    def __next__(self):
        fib = self.first
        if fib > self.max:
            raise StopIteration
        self.first, self.second = self.second, self.first + self.second
        return fib

def main():
    print("\nLimited Fibonacci sequence using a class:")
    for num in Fibonacci(500):
        print(num)

if __name__ == "__main__":
    main()
