import re
from functools import reduce
def sum_of_numbers(input_string):
    arr_digits = re.split(r'[^0-9]', input_string)
    result = reduce((lambda x, y: x + y), [int(n) for n in arr_digits if n.isdigit()])
    return result
    