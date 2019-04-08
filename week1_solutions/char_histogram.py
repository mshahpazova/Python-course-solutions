def char_histogram(string):
    histogram = dict()
    for letter in string:
        if letter not in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    return histogram
    
