'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million(2*10^6).
'''

# Input n: upper bound of the sum

# Create a boolean list (0,1 list) a to indicate whether the index is prime
# Store sum of primes below n in list s

t = int(input().strip())
limit = 2*10**6+1
s = [0] * limit
a = [1] * limit # assume every number below limit is a prime
a[0] = a[1] = 0
for i, isprime in enumerate(a):
    if isprime:
        s[i] = s[i-1] + i
        for n in range(i*i, limit, i):
            a[n] = 0 # label all i multiples as non-prime
    else:
        s[i] = s[i-1]
        
for a0 in range(t):
    n = int(input().strip())
    print(s[n])
