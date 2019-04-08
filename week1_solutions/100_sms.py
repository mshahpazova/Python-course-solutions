def numbers_to_message():
    decoding_hash = {
                     2: ['a', 'b', 'c'],
                     3: [ 'd', 'e', 'f'],
                     4:['g', 'h', 'i'],
                     5: ['j', 'k', 'l'],
                     6: ['m', 'n', 'o'],
                     7: ['p', 'q', 'r', 's'],
                     8: ['t', 'u', 'v'],
                     9: ['w', 'x', 'y', 'z'] }
    arr = [2, -1, 2, 2, -1, 2, 2, 2]
    text = []
    count = 1
    current_num = arr[0]
    next_capital = False
    no_current_num = False
    for index in range(1, len(arr) - 1):
        if no_current_num:
            current_num = аrr[index]
            no_current_num = False
            continue
        if current_num == arr[index]:
            current_num = arr[index]
            count += 1
        else:
            key = decoding_hash[current_num]
            letter_index = (len(arr) - 1) % len(decoding_hash[current_num])
            letter = decoding_hash[key][letter_index]
            if arr[index] == -1:
                no_current_num = True
                text.append(letter)
                count = 0
            elif arr[index] == 0:
                no_current_num = True
                text.append(letter + ' ')
                count = 0
                no_current_num = True
            elif arr[index] == 1:
                next_capital = True
                count = 0
                no_current_num = True
            else:
                text.append(letter)
                count = 0
                current_num = arr[index]
    return ''.join(text)

print(numbers_to_message())