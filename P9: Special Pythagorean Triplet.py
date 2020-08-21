'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# Input n: the sum of a,b,c

# Two conditions can eliminate the free variables to be one.
# Hence one loop is all we need.

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = -1
    if n % 2==0:
        for a in range(3,n//3):
            b = (n**2//2-n*a)//(n-a)
            c = n-a-b
            if a**2+b**2==c**2 and b!=0 and a*b*c>result:
                result = a*b*c
    print(result)
