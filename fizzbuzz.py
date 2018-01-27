#!/usr/bin/env python
import argparse

def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

def print_range(lower, upper):
    for num in range(lower, upper + 1):
        print(fizzbuzz(num))

USAGE = """
How to use FizzBuzz:
    $ python fizzbuzz.py --lowerLimit <lowerLimit> --upperLimit <upperLimit>
"""

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description=None)
    PARSER.add_argument('--lowerLimit', type=int, help='lower limit')
    PARSER.add_argument('--upperLimit', type=int, help='upper limit')

    ARGS = PARSER.parse_args()

    if not(ARGS.lowerLimit and ARGS.upperLimit):
        print(USAGE)
        PARSER.print_help()
        sys.exit(1)

    print_range(ARGS.lowerLimit, ARGS.upperLimit)
