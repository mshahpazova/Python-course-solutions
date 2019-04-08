def prime_factorization(num):
    prime = 2
    prime_dict = {}
    while num > 1:
        while num % prime == 0:
            num = num / prime
            prime_dict[prime] = prime_dict.get(prime, 0) + 1
            print("this is prime", prime)
        prime = find_next_prime(prime)
    return sorted(prime_dict.items())
      

def find_next_prime(prime):
    next_prime = prime + 1
    while not is_prime(next_prime):
        print("this is next prime", next_prime)
        next_prime += 1
    return next_prime

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

assert(prime_factorization(10)== [(2, 1), (5, 1)]) # This is 2^1 * 5^1
assert(prime_factorization(14) == [(2, 1), (7, 1)])
assert(prime_factorization(356) == [(2, 2), (89, 1)])
assert(prime_factorization(89) == [(89, 1)]) # 89 is a prime number
assert(prime_factorization(1000) == [(2, 3), (5, 3)])
print "All tests are OK"