# TODO check for errors, test with more bytes
import os
import sys
def duhs(file_path):
    statinfo = os.stat(file_path)
    gb = statinfo.st_size / 2 ** 30
    print(gb)

def main():
    file_path = sys.argv[1]
    duhs(file_path)

if __name__ == '__main__':
    main()