# too long solution
def is_number_balanced(num)
  first_result = 0
  second_result = 0
  first_count = 0
  second_count = num.length / 2
  while first_count < second_count:
      first_count += 1
      first_result += int(num[first_count])
      if num.length % 2 != 0
          second_count += 1
  while int(second_count <= num.length):
      second_result += int(num[second_count])
      second_count += 1 
      if first_result == second_result:
          return True
      else:
        return False