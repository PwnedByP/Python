'''
Define the function is_prime(n).

n is number that the function is_prime takes as a parameter.

The function is_prime return True if n is a prime number, False otherwise. Such as:
'''

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # Only check odd divisors
        if n % i == 0:
            return False
    return True