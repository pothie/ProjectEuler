'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# Input n: find the nth prime number

t = int(input().strip())
prime = [2,3]
for a0 in range(t):
    n = int(input().strip())
    i = prime[len(prime)-1]
    while len(prime)<n:
        i += 2 #checking odd numbers since last number in prime list
        p = True #Indicator if p is a prime
        for j in prime:
            if j**2>i: # no new prime in the prime factorizaion of i
                break
            elif i%j==0:
                p = False
                break
        if p:
            prime.append(i)
    print(prime[n-1])
    
# Everything involving primes can be improved by solution of Q10.
