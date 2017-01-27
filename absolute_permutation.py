from collections import deque
for _ in range(1):
    a,b=10,5
    lis = list(range(1,a+1))
    if b==0:
        print(*lis)
    elif a%(2*b)==0:
        for i in range(int(a/(2*b))):
            for j in range(b):
                lis[i*2*b + j],lis[i*2*b+b+j]=lis[i*2*b+b+j],lis[i*2*b + j]
        print(*lis)
    else:
        print('-1')

# https://www.hackerrank.com/challenges/absolute-permutation
# the thought process is that in order for the difference between lis[i] and i to be b, I have to swap i with i+b and do (a/(2b)) such operations