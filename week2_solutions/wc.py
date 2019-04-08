# TODO check for errors, test with more bytes
import os
import sys

def count_symbols(file_path):
    f = open(file_path, "r")
    return len(f.read())

def count_words(file_path):
    f = open(file_path, "r")
    words = f.read().split()
    return len(words)

def count_lines(file_path):
    f = open(file_path, "r")
    return len(f.readlines())

def main():
    file_path = sys.argv[2]
    what_is_counted = sys.argv[1]

    if what_is_counted == 'chars':
        print(count_symbols(file_path))
    elif what_is_counted == 'words':
        print(count_words(file_path))
    elif what_is_counted == 'lines':
        print(count_lines(file_path))


if __name__ == '__main__':
    main()