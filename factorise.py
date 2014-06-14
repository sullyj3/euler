import primes
from math import sqrt,ceil

def prime_factors(n):
    '''recursive'''
    
    if primes.is_prime(n):
        return [n]
    
    sqrtn = int(ceil(sqrt(n)))

    first_factor = 2
    while not n % first_factor == 0:
        first_factor += 1

    factor_list = []
    factor_list.extend(prime_factors(first_factor)+prime_factors(int(n/first_factor)))

    return factor_list
