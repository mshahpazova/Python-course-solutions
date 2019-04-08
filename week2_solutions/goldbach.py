# if statements on one line?
def goldbach(n):
    nums_to_check = range(2, n // 2 + 1)
    sums_primes = []
    for num in nums_to_check:
        if is_prime(num) and is_prime(n - num):
            sums_primes.append((num, n - num))
    return sums_primes

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_next_prime(prime):
    next_prime = prime + 1
    while not is_prime(next_prime):
        print("this is next prime", next_prime)
        next_prime += 1
    return next_prime

# print(goldbach(4))
# print(goldbach(6))
# print(goldbach(8))
# print(goldbach(10))
print(goldbach(100))