def parse_input(arr):
  indexes = range(1, len(arr))
  sub_arrays = []
  current_arr = []
  for index in indexes:
    if arr[index] == arr[index - 1]:
      current_arr.append(arr[index - 1])
    else:
      current_arr.append(arr[index - 1])
      sub_arrays.append(current_arr)
      current_arr = []
      if index == len(arr) - 1:
        current_arr = []
  current_arr.append(arr[index])
  sub_arrays.append(current_arr)
  return sub_arrays

assert str(parse_input([2, 2, 2, 2, 2, 2])) == str([[2,2,2,2, 2, 2]])
assert str(parse_input([2, -1, 2, 2, -1, 2, 2, 2])) == str([[2], [-1], [2, 2], [-1], [2, 2, 2]])
assert str(parse_input([2, -1, 2, 2, -1, 2, 2, 2,4])) == str([[2], [-1], [2, 2], [-1], [2, 2, 2],[4]])