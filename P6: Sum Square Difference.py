# Input n: Find the sum square difference of the first n positive numbers

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    soq = (n*(n+1)*(2*n+1))//6
    qos = (n**2*(n+1)**2)//4
    print(qos-soq)
