def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = 12
y = 18
print("GCD:", gcd(x, y))
