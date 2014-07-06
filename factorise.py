import primes
from math import sqrt,ceil
from operator import mul
from functools import reduce

product = lambda x:reduce(mul,x)

def prime_factors(n):
    '''recursive'''
    
    # base case
    if primes.is_prime(n):
        return [n]
    
    sqrtn = int(ceil(sqrt(n)))

    first_factor = 2
    while not n % first_factor == 0:
        first_factor += 1

    factor_list = []
    factor_list.extend(prime_factors(first_factor)+prime_factors(int(n/first_factor)))

    return factor_list

def factors(n): #unfinished. Probably needs a rewrite

    '''
    todo:
    - fix faulty algorithm.
        - incomplete: fails factors(500) (leaves out 10*50)

    - come up with way of only generating unique factors in order to save 
      uniqueifying at the end

    '''
    
    p_factor_list = prime_factors(n)
    factor_pair_list = [(1,n)]

    #given p_factor_list of length 3: eg [2, 3, 5] (n=30):
    # 6 * 5
    # 2 * 15

    #what about length 4? eg [2, 3, 5, 5] (n=150)
    # (2*3) * (5*5)
    # (2*5) * (3*5)

    # dict containing (prime_factor : number of occurences in prime factorization of n)
    p_factor_count = { i:p_factor_list.count(i) for i in set(p_factor_list) }
    
    #import pdb; pdb.set_trace()

    for prime_factor in set(p_factor_list):
        
        num_occurences = p_factor_count[prime_factor]
        
        # problem here, I think. need to be multiplying by numbers other than 
        # itself to get all factors

        for power in range(1,num_occurences+1):
            factor1 = prime_factor ** power
            factor_pair = (factor1, int(n / factor1) )
            # sort, to enable checking for identity later 
            # (order doesn't matter when checking for identity of factor pairs)
            factor_pair = tuple(sorted(factor_pair))

            factor_pair_list.append(factor_pair)

    #use set, since we only want unique factors
    factor_set = set()
    for pair in factor_pair_list:
        for factor in pair:
            factor_set.add(factor)

    factor_list = sorted(factor_set)
    return factor_list
