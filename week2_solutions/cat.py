# cat.py
import sys
import os
def cat(file_path):
    f = open(file_path, "r")
    lines = f.readlines()
    for line in lines:
        print(line, end='')

def main():
    file_path = sys.argv[1]
    cat(file_path)

if __name__ == '__main__':
    main()