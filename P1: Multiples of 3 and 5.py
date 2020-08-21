
# Input t: the upper bound of multiples of 3 and 5

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
