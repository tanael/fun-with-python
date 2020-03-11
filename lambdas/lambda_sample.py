#!/usr/bin/env python3

from functools import reduce

def main():
    numbers = [1, 3, 9, 7, 33, 9732, 92, 34, 10, 230]
    multiples_of_3 = list(filter(lambda x: (x % 3 == 0), numbers))
    print(multiples_of_3)
    squared = list(map(lambda x: x**2, numbers))
    print(squared)
    product = reduce((lambda x, y: x * y), numbers)
    print(product)

if __name__ == "__main__":
    main()
