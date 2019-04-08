def is_credit_card_valid(number):
    if len(str(number)) % 2 == 0:
        return False
    arr_str_digits = list(str(number))
    arr_ints = map(lambda x: int(x), arr_str_digits)
    print(list(arr_ints))
    sum_nums = 0
for idx, val in enumerate(arr_ints):
        sum_nums += val * (idx % 2 + 1)
    str_result = str(sum_nums)
    print(str_result[len(str_result) - 1])
    print(str_result)
    if str_result[len(str_result) - 1] == '0':
        return True
    else:
        return False

print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))

# >>> is_credit_card_valid(79927398713)
# True
# >>> is_credit_card_valid(79927398715)
# False