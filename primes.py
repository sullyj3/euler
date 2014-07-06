from math import sqrt,ceil

'''ideas:
Could I continue an already existing sieve?'''

#todo: write a version of sieve which can utilise an existing list of primes

verbosity = 0
def debug_print(text, min_verb):
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

        debug_print("appending {0}. we now have {1} primes".format(next_prime, primes_len), 1)
        primes.append(next_prime)
        primes_len += 1

    return primes

def sieve(n, composites = False):
    '''is inclusive of n. ie, returned list will include n if n is prime.'''

    nums = [0,1]+[True for i in range(2,n+1)]

    sqrtn = int(ceil(sqrt(n)))
    
    #first prime
    current_prime = 2

    while True: #terminating condition in except StopIteration: below

        #mark all multiples of current_prime as composites, then make current_prime
        #the next prime above itself, until there are no more primes below n.

        for index in range(current_prime**2, n+1, current_prime):
            nums[index] = False

        # there's got to be a nicer way of doing this.
        # Construct a generator for the sole purpose of figuring out the next
        # prime. then do a gen.next() excepting stop iteration (meaning no more
        # primes below n)

        primes_upto_sqrtn = (ind for ind,is_prime in list(enumerate(nums))[current_prime + 1:sqrtn + 1] if is_prime)
        try:
            current_prime = next(primes_upto_sqrtn)
        except StopIteration:
            break
    
    if not composites:
        return [ind for ind,is_prime in list(enumerate(nums))[2:] if is_prime]
    else:
        return [ind for ind,is_prime in list(enumerate(nums))[2:] if not is_prime]

def sieve_2(n, primes = None, composites = False): #needs a better name.
    # version of sieve which takes a list of primes we've already found.

    # if last element of existing prime list is >= n: return list of primes
    # truncated so n is last element
    if primes[-1] >= n:
        ret = []
        for i in primes:
            if i <= n:
                ret.append(i)
            else:
                return ret
        
    # construct an n long list of boolean values representing whether or not
    # the index is prime.

    # make sure each number corresponds to its index in the list
    nums = [0,1]

    # assume each number between the smallest and largest prime in primes is 
    # composite unless that number is present in primes
    nums += [False for i in range(2,primes[-1]+1)]
    for p in primes:
        nums[p] = True

    # assume all numbers greater than the largest prime are composite until 
    # proven otherwise
    nums += [True for i in range(primes[-1]+1, n+1)]

    # mark all multiples of each prime p greater than the largest (last) 
    # prime in our input list as composite
    for p in primes: # while p < sqrtn
    # this is another case where a for-while loop would be useful.

        position = p**2
        # move beyond last prime
        while position <= primes[-1]:
            position += p
        while position <= n:
            nums[position] = False
            position += p
        
        

def find_next_prime(primes): #todo: refactor to use is_prime(), prevent invalid input
    '''takes a list of primes. primes must contain a sequential list
    of all the primes between 0 and the next one you want to find
    '''

    #primes except 2 are always odd. start looking at the number which is two 
    #greater than the last prime found.
    #(this function won't work if primes == [2] )

    next_check = primes[-1] + 2
    while True:
        #test next number for primality.

        debug_print("next number to be checked for primality is {0}".format(next_check), 2)

        #####################################################################
        #problem is, this doesn't take advantage of the list of primes that 
        #I've already passed to find_next_prime, since is_prime generates 
        #it's own list every time. if i'm calling it many times (ie in a 
        #fuckin while true loop), that's gonna be pretty inefficient. I should
        #really have a globally accessible list which can be written to a file.

        if is_prime(next_check): 
            return next_check
        else:
            next_check += 2

        #up_to_sqrt = (prime for prime in primes if prime <= sqrt(next_check) )
        #
        #for prime in up_to_sqrt:
        #    if next_check % prime == 0:
        #        debug_print("{0} is not prime (divisible by {1})".format(next_check, prime), 2)
        #        next_check += 2
        #        break
        #else:
        #    debug_print("{0} is prime!".format(next_check), 2)
        #    return next_check

def is_prime(n,primes=None):
    if n in (2,3):
        return True

    sqrtn = int(ceil(sqrt(n)))

    #optionally take existing list of primes to speed computation time
    if primes:
        if primes[-1] < sqrtn:
        #find the rest up to sqrtn. Perhaps upgrade sieve to use existing list
        #of primes (optionally)
            pass
        elif primes[-1] > sqrtn:
            #construct new list containing only primes up to sqrtn
            pass
        elif primes[-1] == sqrtn:
            #um
            pass

    #if a number is divisible by a non prime, it is also divisible by all its prime factors
    #therefore we only need to test if divisible by primes
    #additionally, we only need to test for divisibility by numbers less the square root
    #of the one we're testing

    
    up_to_sqrt = sieve(sqrtn) #inclusive of sqrtn
    for prime in up_to_sqrt:
        if n % prime == 0:
            debug_print("{0} is not prime (divisible by {1})".format(n, prime), 2)
            return False
    else:
        debug_print("{0} is prime!".format(n), 2)
        return True
