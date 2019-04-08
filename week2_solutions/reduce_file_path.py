import os
import sys
def reduce_file_path(file_path):
    splitted_path = file_path.split('/')
    cleared_path = list(filter(lambda x: x != '' and x != '.', splitted_path))
    reduced_path = []
    for element in cleared_path:
        if element == '..':
            reduced_path.pop()
        else:
            reduced_path.append(element)
    return('/' + '/'.join(reduced_path))

def main():
    file_path = sys.argv[1]
    print(reduce_file_path(file_path))

if __name__ == '__main__':
    main()