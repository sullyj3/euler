verbosity = 1

function debug_print(text,min_verb)
    if verbosity >= min_verb
        println(text)
    end
end

function find_n_primes(n::Integer)

    #=  perhaps I should store primes in a file for reference? Saves computation.
        ie, I only need to find the next prime If i've never found it before, 
        otherwise I can just look it up.

        in that case I'd have to make certain that I never make any errors, or i'd start
        storing incorrect primes 
    =#

    primes = Integer[2, 3]
    primes_len = length(primes)
    while primes_len < n
        next_prime = find_next_prime(primes)
        push!(primes,next_prime)
        primes_len += 1
        debug_print("appending $(next_prime). we now have $(primes_len) primes", 1)
    end 

    primes
end
    
function find_next_prime(primes)
    #=  takes a list of primes. primes must contain a sequential list
    of all the primes between 0 and the next one you want to find

    primes except 2 are always odd. start looking at the number which is two 
    greater than the last prime found.
    (this function won't work if primes == [2] ) =#

    current_check = primes[end] + 2
    while true
        #=  test next number for primacy.
        if a number is divisible by a non prime, it is also divisible by all its prime factors
        therefore we only need to test if divisible by primes
        additionally, we only need to test for divisibility by numbers less the square root
        of the one we're testing    =#

        debug_print("next number to be checked for primacy is $(current_check)", 2)

        up_to_sqrt = Integer[]
        square_root = sqrt(current_check)
        pos = 1

	primes_index = 1
	while primes_index <= length(primes)
	    if 
        for i in primes
            if i <= square_root
                push!(up_to_sqrt, i)
            else
                break
            end
        end

        #for prime in up_to_sqrt
        #    if current_check % prime == 0
        #        debug_print("$(current_check) is not prime (divisible by $(prime))", 2)
        #        current_check += 2
        #        break
        #    end
        #end
        else
            debug_print("{0} is prime!".format(current_check), 2)
            return current_check
