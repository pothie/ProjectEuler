'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Input n: We are looking for the smallest positive number that is evenly divisible by all integers in [1,n] 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = []
    
    # Find the prime factorization of each integer < n
    # Get rid of duplicated primes and record p^k in result
    for i in range(2,n+1):
        temp = 1
        for j in result:
            if i%j == 0 and temp <i:
                temp *= j #keep track of primes that are already in the prime list
        if i//temp>1: % if a new prime or a new appearence of any prime pops out
            result.append(i//temp)
    s = 1
    for x in result:
        s *=x
    print(s)
