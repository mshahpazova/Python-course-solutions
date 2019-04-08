# generate_numbers.py
import sys
import os
import random

def generate_numbers(filename, numbers):
    # if not os.path.exists(filename):
        # os.mknod(filename)
    file = open(filename, "w+")
    arr_nums = random.sample(range(1, 100), numbers)
    print(''arr_nums)
    # numbers = list(map(lambda x : randint(0, 1000), range(0, numbers))
    ile.write(''.join(arr_nums))
            



def main():
    filename = sys.argv[1]
    numbers = int(sys.argv[2])
    generate_numbers(filename, numbers)

if __name__ == '__main__':
    main()