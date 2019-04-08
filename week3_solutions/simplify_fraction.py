def simplify_fraction(fraction):
    numerator, denomerator = fraction
    def gcd(a,b):
        if a < b:
            return gcd(b, a)
        if b == 0:
            return a
        else:
            return gcd(a - b, b)
    gcd = gcd(numerator, denomerator)
    return (numerator // gcd, denomerator // gcd )

print(simplify_fraction((4,12)))