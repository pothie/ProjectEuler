
# Input t: the upper bound of the Fibonacci sequence  
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    F = [2,8]
    while (4*F[len(F)-1]+F[len(F)-2])<n:
        new = 4*F[len(F)-1]+F[len(F)-2]
        F.append(new)
        
    print(sum(F))

# Even Fibonacci numbers appear every three numbers in the Fibonacci sequence. 
# By extracting those even numbers from the sequence, a parttern F_n = 4F_(n-1) +F_(n-2) is observed, which extends the parttern of Fibonacci sequence.
# Similar to P1, the above algorithm runs faster than looping through every (even) number.
