from functools import reduce

def sum_matrix(m):
    result = 0
    for sub_list in m:
        result += reduce((lambda x, y: x + y), sub_list)
    print(result)
    return result

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_matrix(m)
