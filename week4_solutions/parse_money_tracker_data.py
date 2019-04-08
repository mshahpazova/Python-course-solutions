def read_file():
    f = open('money_tracker.txt', 'r')
    lines = f.readlines()
    f.close()
    return lines

