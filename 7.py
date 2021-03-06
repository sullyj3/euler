from math import sqrt

verbosity = 1
def debug_print(text,min_verb):
    if verbosity >= min_verb:
        print(text)

def find_n_primes(n):
    assert type(n) is int and n > 0

    #perhaps I should store primes in a file for reference? Saves computation.
    #ie, I only need to find the next prime If i've never found it before, 
    #otherwise I can just look it up.

    #in that case I'd have to make certain that I never make any errors, or i'd start
    #storing incorrect primes

    primes = [2, 3]
    primes_len = len(primes)
    while primes_len < n:
        next_prime = find_next_prime(primes)
        primes.append(next_prime)
        primes_len += 1
        debug_print("appending {0}. we now have {1} primes".format(next_prime, primes_len), 1)
    return primes
    
def find_next_prime(primes):
    '''takes a list of primes. primes must contain a sequential list
    of all the primes between 0 and the next one you want to find
    '''

    #primes except 2 are always odd. start looking at the number which is two 
    #greater than the last prime found.
    #(this function won't work if primes == [2] )

    next_check = primes[-1] + 2
    while True:
        #test next number for primacy.
        #if a number is divisible by a non prime, it is also divisible by all its prime factors
        #therefore we only need to test if divisible by primes
        #additionally, we only need to test for divisibility by numbers less the square root
        #of the one we're testing

        debug_print("next number to be checked for primacy is {0}".format(next_check), 2)

        up_to_sqrt = (prime for prime in primes if prime <= sqrt(next_check) )

        for prime in up_to_sqrt:
            if next_check % prime == 0:
                debug_print("{0} is not prime (divisible by {1})".format(next_check, prime), 2)
                next_check += 2
                break
        else:
            debug_print("{0} is prime!".format(next_check), 2)
            return next_check
