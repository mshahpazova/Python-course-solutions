# cat2.py
import sys
import os
def cat_multiple(args):
    for file_path in args:
      print_file(file_path)

def print_file(file_path):
    f = open(file_path, "r")
    lines = f.readlines()
    for line in lines:
        print(line, end='')
    print()
    
def main():
    file_paths = sys.argv
    cat_multiple(file_paths)

if __name__ == '__main__':
    main()