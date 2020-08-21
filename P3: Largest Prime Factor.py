# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Input t: the number whose largest prime factor is our answer

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime = 1
    
    # Check if n is even
    while n%2== 0:
        n //= 2
        prime = 2
        
    # n is odd now, check odd numbers
    for i in range(3,int(n**0.5+1),2): 
        while n%i==0:
            n //= i
            prime = i
            
    # the number left(n) is either 1 
    # or a prime number not on the our list(largest prime number)
    if n==1:
        print(prime)
    else:
        print(n)
        
# Running time can be improved because all odd numbers are too many for primes. 
# See solution for P4 or P5.
