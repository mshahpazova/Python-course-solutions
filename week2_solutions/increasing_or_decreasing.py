def increasing_or_decreasing(seq):
    diff_arr = []
    indexes = range(1, len(seq))
    for index in indexes:
        diff_arr.append(seq[index] - seq[index - 1])
    print(diff_arr)
    if diff_arr[0] > 0 and diff_arr[len(diff_arr) - 1] > 0:
        return "Up!"
    elif diff_arr[0] < 0 and diff_arr[len(diff_arr) - 1] < 0:
        return "Down!"
    else: return False

print(increasing_or_decreasing([1,2,3,4,5]))
# Up!
print(increasing_or_decreasing([5,6,-10]))
# False
print(increasing_or_decreasing([1,1,1,1]))
# False
print(increasing_or_decreasing([9,8,7,6]))
# Down!