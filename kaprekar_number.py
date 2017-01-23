from math import ceil
a,b = int(input()),int(input())
lis = []
for i in range(a,b+1):
    c = i**2
    divisor = 10**(ceil(len(str(c))/2))
    if int(c/divisor) + int(c%divisor) == i:
        lis.append(i)
if len(lis)>0
    print(*lis)
else:
    print("INVALID RANGE")

# given a range, print the kaprekar numbers in this range. If there's no kaprekar number in the given range, print "INVALID RANGE"
# Wiki definition of kaprekar numbers:In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.