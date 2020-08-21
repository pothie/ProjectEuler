# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import sys

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    m3 = (((n-1)//3)*((n-1)//3+1))//2*3
    m5 = (((n-1)//5)*((n-1)//5+1))//2*5
    m15 = (((n-1)//15)*((n-1)//15+1))//2*15
    print(m3+m5-m15)

# Arithmic operation saves time compared to looping through all numbers lesss than t.
# //(integer division) here saves a lot of time compared to (/) float division. 
