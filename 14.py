def collatz(n,depth):
    depth += 1 #when calling initial, use depth = 0
    if n == 1:
        return n,depth
    elif n%2: #is odd
        return collatz(3*n + 1,depth)
    else: #is even
        return collatz(n/2,depth)

def longest_chain_start_under_n(n, method = 'recursive'):
    longest_chain = 0
    longest_chain_start = None

    if method == 'recursive':

        for start in range(1,n):
            #print("start = {0}".format(i))
            depth = collatz(start,0)[1]
            if depth > longest_chain:
                longest_chain, longest_chain_start = depth, start

    elif method == 'iterative':

        depth = 0
        for start in range(1,n):
            #print("start = {0}".format(start))
            i = start
            while not i == 1:
                depth += 1
                if i%2: #is odd
                    i = 3*i + 1
                else: #is even
                    i /= 2

            if depth > longest_chain:
                longest_chain, longest_chain_start = depth, start

    return longest_chain_start, longest_chain
