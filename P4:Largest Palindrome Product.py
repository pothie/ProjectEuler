#Input t: upper bound of the palindrome number

t = int(input().strip())

# create a palindrome number list where every element in it is a product of two three-digit numbers
palin = []
for n in range(101,1000):
    for m in range(101,1000):
        if str(m*n) == str(m*n)[::-1]:
            palin.append(m*n)
palin = sorted(palin)

# Loop through palindrome list
for a0 in range(t):
    n = int(input().strip())
    result = 0
    i = 0
    while result < n:
        result = palin[i]
        i += 1
    print(palin[i-2])
    
# Faster than looping through every palindrome number and check if it is a product of two 3-digit number.
# Because that involves float division, which slows down the process.
