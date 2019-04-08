def sum_of_digits(n):
    num_str = str(n)
    num_arr = list(num_str)
    if num_arr[0] == '-':
        num_arr.pop(0)
    indexes = range(len(num_arr) - 1 )
    result = 0
    for num in num_arr:
        result += int(num)
    return result
    

# print(sum_of_digits(-1234))

def to_digits(n):
    items = str(n)
    digits = list(map(lambda x: int(x), items))
    return digits
    

def to_number(digits):
    str_num = ''.join(str(v) for v in digits)
    return int(str_num)
    

def  factorial(digit):
    nums = range(1, digit + 1)
    result = 1
    if digit == 0:
      return 1
    for num in nums:
        result *= num
    return result

def factorial_digits(num):
    digits = to_digits(num)
    sum_factorials = 0;
    for digit in digits:
        sum_factorials += factorial(digit)
    return sum_factorials

def palindrome(n):
    string_pal = str(n).lower()
    indexes = range(len(string_pal))
    reversed_indexes = list(reversed(indexes))
    all_matched = True
    for index in indexes:
        print("index", string_pal[index])
        print("reversed", string_pal[reversed_indexes[index]])
        if string_pal[index] != string_pal[reversed_indexes[index]]:
            all_matched = False
    return all_matched
    
def palindrome_best(n):
    string_pal = str(n).lower()
    for index in range(len(string_pal)/2):
        if string_pal[index] != string_pal[-index-1]:
            return False
    return True


def count_vowels(string):
    vowels = 'aeiouy'
    string = string.lower()
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count

def sum_matrix(m):
    sum = 0
    for row in m:
      for col in row:
        sum += col
    return sum

# def group(arr):
#     groups = {}
#     result = []
#     for item in arr:
#         groups[item] = groups.get(item, 0) + 1
#     for key in groups:
#         result.append([key] * groups[key])
#     return result

def group(arr):
  indexes = range(0, len(arr) + 1)
  small_arr = []
  big_arr = []
  for item in arr:
      if small_arr == []: small_arr.append(item)
      elif (small_arr[len(small_arr) - 1]) == item: small_arr.append(item)
      else:
        big_arr.append(small_arr)
        small_arr = []
        small_arr.append(item)
  big_arr.append(small_arr)
  return big_arr

def max_consecutive(items):
    return max(len(item) for item in group(items))

def nan_expand(times):
    result = "Not a "
    if times == 1:
        result += "NaN"
    else:
        result += nan_expand(times - 1)
    return result

# ivan
# 5 4
# i v a n
# e v n h
# i n a v
# m v v n
# q r i t
# range(len(string_pal)/2):
def test():
    pattern = input()
    size = input()
    print(size[0])
    for index in range(int(size[0])):
        row = input()
        print(row)

test()

# print(nan_expand(2))
  # try:
  #   return max((sum(1 for _ in group), -i, item) for i, (item, group) in enumerate(groupby(iterable)))[2]
  # except ValueError:
  #   return None
# print(group([1, 1, 1, 2, 3, 1, 1]))
# def char_histogram(string):
#     out = {}
#     for c in string:
#         out[c] = out.get(c, 0) + 1
#     return out

# print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))

# print(count_vowels("maria"))
# def palindrome_best(n):
#     string_pal = str(n).lower()
#     for index in range(len(string_pal)):
#         if string_pal[index] != string_pal[-index-1]:
#             return False
#     return True

# assert palindrome_best("asa")
# assert palindrome_best("assa")
# assert palindrome_best("asdffdsa")
# assert not palindrome_best("asdffdsa?")
# print "Tests are OK!"

# def palindrome(n):
#     string_pal = str(n).lower()
#     indexes = range(len(string_pal))
#     all_matched = True
#     for index in indexes:
#         rev = len(string_pal)- index - 1
#         if string_pal[index] != string_pal[rev]:
#             all_matched = False
#     return all_matched



# print(palindrome(12321))


# print(factorial(3))
# print(factorial_digits(999))
# print(to_digits(1234))