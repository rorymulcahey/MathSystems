'''

Primes: int[] GetPrimes(int n)
Give a function to give a list of primes up to the n-th.
Can be solved using various methods.

'''

import math


def get_primes(instances):
    lst = [2]
    for x in range(1, instances):
        num = 1 + 2*x
        prime = True
        for y in range(2, int(math.sqrt(num))+1):
            if num % y == 0:
                print(num)
                prime = False
                break
        if prime:
            lst.append(num)
    return lst


print(get_primes(1000))
