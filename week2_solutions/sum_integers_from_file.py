# sum_integers_from_file.py
import sys

from functools import reduce
def sum_numbers(filename):
    f = open(filename, "r")
    lines = f.readlines()
    nums = map(lambda x : int(x), lines[0].split(' '))
    sum_ints = reduce((lambda x, y: x + y), nums)
    print(sum_ints)
    # numbers = list(map(lambda x : randint(0, 1000), range(0, numbers))

def main():
    filename = sys.argv[1]
    sum_numbers(filename)

if __name__ == '__main__':
    main()