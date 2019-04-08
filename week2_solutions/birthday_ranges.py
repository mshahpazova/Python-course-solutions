# to solve this one in a different way -> checking each number separately, and not each range separately
def birthday_ranges(birthdays, ranges):
      list_all_occurances = []
      for range in ranges:
          occurances = 0
          for birthday in birthdays:
              if birthday >= range[0] and birthday <= range[1]:
                occurances += 1
          list_all_occurances.append(occurances)
      return list_all_occurances

print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# [2, 3, 4, 5, 2]
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))
# [5, 2, 0, 1]