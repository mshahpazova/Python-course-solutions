# collect_fractions.py
from functools import reduce
def gcd(a,b):
        if a < b:
            return gcd(b, a)
        if b == 0:
            return a
        else:
            return gcd(a - b, b)

def simplify_fraction(fraction):
    numerator, denomerator = fraction
    _gcd = gcd(numerator, denomerator)
    return (numerator // _gcd, denomerator // _gcd )

def nok(nums):
  if len(nums) == 1:
      return nums[0]
  if len(nums) == 2:
      return (nums[0] * nums[1]) //  gcd(nums[0], nums[1])
  return nok([nums[0], nok(nums[1:])])

def expand_fraction(fraction, new_bottom):
    top, bottom = fraction
    new_top = top * new_bottom // bottom
    return (new_top, new_bottom)

def collect_fractions(fractions):
    denominators = list(map(lambda fraction : fraction[1], fractions))
    new_denominator = nok(denominators)
    expanded_fractions = map(lambda fraction : expand_fraction(fraction, new_denominator), fractions)
    sum_numerators = reduce(lambda x, y : x + y, map(lambda fraction : fraction[0], expanded_fractions))
    return simplify_fraction((sum_numerators, new_denominator))

print( collect_fractions([(1, 4), (1, 2)]))
# (3, 4)
print( collect_fractions([(1, 7), (2, 6)]))