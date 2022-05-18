from math import sqrt


def prime_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for x in range (3, int(sqrt(n))+1, 2):
            if (n % x == 0):
                return False
        return True

print(prime_number(121))
